#!/usr/bin/python
import urllib3

print """
 _       ______     __________   _______           __         
| |     / / __ \   / ____/  _/  / ____(_)___  ____/ /__  _____
| | /| / / /_/ /  / /    / /   / /_  / / __ \/ __  / _ \/ ___/
| |/ |/ / ____/  / /____/ /   / __/ / / / / / /_/ /  __/ /    
|__/|__/_/       \____/___/  /_/   /_/_/ /_/\__,_/\___/_/     

 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 +    Name        : Wordpress Content Injection Finder      +
 +    Author      : Rudra Sarkar                            +
 +    Date        : 04/02/2017                              +
 +    Description : Wordpress 4.7.0 & 4.7.1 Content         +
 +                  Injection Vulnerability -               +
 +                  found by Sucuri Labs -                  +
 +                  An unauthenticated user can change the  +
 +                  contents of any blog post with a single +
 +                  POST request.                           +
 +                                                          +
 +                  Thanks To Sucuri Labs :)                +
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
 For Inject https://blog.sucuri.net/2017/02/content-injection-vulnerability-wordpress-rest-api.html
      """

# Enter your URL
u = raw_input('Enter The URL > ')

http = urllib3.PoolManager()

# Param of wp json
param = "/index.php/wp-json/wp/v2/posts/"

# URL Checker ;)
bugs = http.request('GET', u + param )

# Website Data Reader
if "guid" in bugs.data:
		print "\n [+] Content Injection Success :D"
		print "\n [+] POC: ", u + param
else:
		print "\n [!] Website Are Not Vulnerable at CI"
