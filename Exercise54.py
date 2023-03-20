'''Assuming that we have some email addresses in the ”username@companyname.com”
format, please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only'''

import re

li = "username@companyname.com username@companyname.com username@companyname.com username@companyname.com username@companyname.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern, li)

print(ans)