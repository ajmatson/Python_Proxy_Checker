#!/usr/bin/env python
"""
This script is designed to analyse a test a proxy for specific content from an outside page. The proxies are read from a list from a file specified
in the proxy_list_location variable below. Please also fill in the other information such as the URI to test from that has the string, the string to
check of course, and the proxy auth information needed.

Latest Revision 1.8.0:
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
__version__ = '1.8.0'
__status__ = 'QA Testing'



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_alert(proxyname, smtp_domain, addr_to, addr_from, smtp_server):
    ehlo_string = "%s" % smtp_domain
    message = MIMEMultipart('alternative')
    message['To'] = ", ".join(addr_to)
    message['From'] = addr_from
    message['Subject'] = "Proxy Alert for: %s" % proxyname
    text = "The proxy at %s has failed the URL check, please investigate immediately!" % (proxyname)
    html = '''\
        <html>
      <head></head>
      <body>
         <p>The proxy at %s has failed the URL check <br />
                 Please investigate immediately!!
         </p>
      </body>
    </html>
    ''' % (proxyname)
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)

    send = smtplib.SMTP(smtp_server)
    send.ehlo(ehlo_string)
    #send.esmtp_features["auth"] = "LOGIN PLAIN"
    #send.login(smtp_user,smtp_pass)
    send.sendmail(addr_from, addr_to, message.as_string())
    send.quit()
