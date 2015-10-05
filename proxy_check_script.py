#!/usr/bin/env python

"""
This script is designed to analyse a test a proxy for specific content from an outside page. The proxies are read from a list from a file specified
in the proxy_list_location variable below. Please also fill in the other information such as the URI to test from that has the string, the string to
check of course, and the proxy auth information needed.

Latest Revision 1.8.1:
    - Cleaned up some code and fixed a few backend issues.

Revision 1.8.0:
    - Added the ability to add the port to the proxylist.txt and have it parse (eg. 1.1.1.1:3128) allowing for different proxy ports to be used for multiple proxies.
    - Added some additional logging.
    - Cleaned up code a bit more.

Revision 1.7.1:
    - Added NTLM/Kerberos Support for Proxy Authentication.
    - Cleaned up code and added better comments.

Revision 1.7.0:
    - Added support for Alert Emails to be sent with SMTP Module.
"""
__author__ = 'Alan J. Matson'
__email__ = 'alan@echotek.us'
__copyright__ = 'Copyright 2015, EchoTEK Solution'
__license__ = 'GPL'
__version__ = '1.8.1'
__status__ = 'QA Testing'

# Import the modules needed for the script
import urllib2, sys, datetime
from smtptest import send_alert

# Set the initial variables for use
uri = "http://www.domain.com/check.txt"
proxy_list_location = "proxylist.txt"
proxy_server = "NULL"  # DO NOT CHANGE, USED TO INITALIZE THE VARIABLE
proxy_port = "NULL"    # DO NOT CHANGE, USED TO INITALIZE THE VARIABLE
proxy_realm = proxy_server
proxy_user = "proxy_user"
proxy_password = "proxy_pass"

# Setup the SMTP details, Change accordingly and make sure the script can relay to SMTP Server.
smtp_domain = 'sendingdomain.com'
addr_to = ['addr1@domain.com','addr2@dmain.com']
addr_from = 'addrfrom@amatson.lan'
smtp_server = 'smtpserver.domain.com'

check_string = 'RANDOM_STRING'  # Change to match the string stored on your URI

# Setup the date/time for the logging
dt = datetime.datetime.now()
date_time = dt.strftime('%Y/%m/%d %H:%M:%S')

# Log file location
lf_location = '/var/log/proxy_checker.log'

codeauth = "W4SO4-30SD1-BHS5S-10E98-CFEEB"




# ============================================================================================================
# DO NOT MODIFY BELOW THIS LINE OR THE CODE MAY BREAK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ============================================================================================================


def proxy_test(proxy_server):
    proxy_server2, proxy_port2 = proxy_server.split(':')
    full_proxy_string = "http://%s:%s@%s:%s" % (proxy_user, proxy_password, proxy_server2, proxy_port2)
    response = "null"
    try:
        proxy_handler = urllib2.ProxyHandler({"http": full_proxy_string})

        proxy = urllib2.build_opener(proxy_handler)
        proxy.addheaders = [
            ('User-agent', 'Mozilla/5.0 Python/2.7 ProxyCheck/1.8.1 Code/' + codeauth),
            ('Pragma', 'no-cache'),
            ('X-Reqested-By', 'Proxy Check Script'),
            ('X-Powered-By', 'ProxyCheck.ns')
        ]
        urllib2.install_opener(proxy)
        connection = urllib2.urlopen(uri, timeout = 60)
        response = connection.read()
        response = response.strip()
    except urllib2.HTTPError, err:
        if err.code == 407:
            print "HTTP RESPONSE 407: Proxy authentication required, please ensure correct username and password"
            sys.exit(407)
        if err.code == 502:
            print "HTTP RESPONSE 502: No route to host, verify proxy can reach the test URI"
            sys.exit(502)
    except urllib2.URLError:
        print "Proxy check failed for " + proxy_server + ". Sending email alert!"
        with open(lf_location, "a") as log_file:
            log_file.write(date_time + " - " + "Proxy checked failed for " + proxy_server + ". Sending email alert!" + "\n")
        send_alert(proxy_server, smtp_domain, addr_to, addr_from, smtp_server)

    if response == check_string:
        print "Response string matches: " + response
        print "Proxy connection successful for user %s via proxy %s" % (proxy_user, proxy_server)
        with open(lf_location, "a") as log_file:
            log_file.write("%s - Proxy connection successful for user %s via proxy %s \n" % (date_time,proxy_user, proxy_server))
    elif response == "null":
        print ""
    else:
        print "Response string does not match: " + response
        print "Proxy connection failed for %s" % (proxy_server)
        print "HTTP Response Code was: "
        send_alert(proxy_server, smtp_domain, addr_to, addr_from, smtp_server)
    return 0


if __name__ == "__main__":
    for proxies in open(proxy_list_location):
        proxy = proxies.strip()
        if not proxy.startswith('#'):
            proxy_test(proxy)
