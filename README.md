# Python Proxy Checker v1.8.1<br />
A set of python scripts (written for Python 2.7) to test proxy traffic and alert if down. Good for Security Admins for live proxy monitoring as it tests the actually traffic for a string on the internet not just if the proxy is up. Originally this was written for Websense Content Gateway proxies but can be tailored to virtually any proxy. You need an webserver with a flat file and a single string with no line breaks to query against. Currently the scripts need to be all downloaded and the proxies added to the proxylist.txt file (notice bad proxies can be excluded from check with a # in front of them):

Example for proxylist.txt file: <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy1.domain.com:8080 <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy2.domain.com:3128 <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy3.domain.com:1234 <br />
&nbsp;&nbsp;&nbsp;&nbsp;#badproxy.domain.com:8080 <br />
  

To run the script you need to setup a CRON job for your desired time for example: <br />
&nbsp;&nbsp;&nbsp;&nbsp;0,30 * * * * /proxy_check_script.py /dev/null 2>&1
  

This script is provided as is and no expressed support or warranty. I will help if can but not guaranteed. License is GPL and content can be modified as long as credit is given by not removing the script headers.


New Features Planned for v2.0:<br />
&nbsp;&nbsp;&nbsp;&nbsp;- Better logging, detailed email alerts <br />
&nbsp;&nbsp;&nbsp;&nbsp;- Installer including auto creating proxylist.txt based on installer prompting for information. <br />
&nbsp;&nbsp;&nbsp;&nbsp;- Logging moved to /var/log and setting up logrotate 
