# Python_Proxy_Checker
A set of python scripts to test proxy traffic and alert if down. Good for Security Admins for live proxy monitoring. Currently the scripts need to be all downloaded and the proxies added to the proxylist.txt file (notice bad proxies can be excluded from check with a # in front of them):

Example for proxylist.txt file:
	proxy1.domain.com:8080
	proxy2.domain.com:3128
	proxy3.domain.com:1234
	#badproxy.domain.com:8080
  

To run the script you need to setup a CRON job for your desired time for example:
	0,30 * * * * /proxy_check_script.py /dev/null 2>&1
  

This script is provided as is and no expressed support or warranty. I will help if can but not guaranteed. License is GPL and content can be modified as long as credit is given by not removing the script headers.
