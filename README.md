# Python_Proxy_Checker <br />
A set of python scripts to test proxy traffic and alert if down. Good for Security Admins for live proxy monitoring. Currently the scripts need to be all downloaded and the proxies added to the proxylist.txt file (notice bad proxies can be excluded from check with a # in front of them):

Example for proxylist.txt file: <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy1.domain.com:8080 <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy2.domain.com:3128 <br />
&nbsp;&nbsp;&nbsp;&nbsp;proxy3.domain.com:1234 <br />
&nbsp;&nbsp;&nbsp;&nbsp;#badproxy.domain.com:8080 <br />
  

To run the script you need to setup a CRON job for your desired time for example: <br />
&nbsp;&nbsp;&nbsp;&nbsp;0,30 * * * * /proxy_check_script.py /dev/null 2>&1
  

This script is provided as is and no expressed support or warranty. I will help if can but not guaranteed. License is GPL and content can be modified as long as credit is given by not removing the script headers.


New Features Planned: <br />
&nbsp;&nbsp;&nbsp;&nbsp;- Better logging, detailed email alerts
&nbsp;&nbsp;&nbsp;&nbsp;- Installer including auto creating proxylist.txt based on installer prompting for information.
&nbsp;&nbsp;&nbsp;&nbsp;- Logging moved to /var/log and setting up logrotate
