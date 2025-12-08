# 10. Write a Python program to validate: 
#  Email: "user@gmail.com" 
#  URL: "https://www.python.org" 
# using regex. 

import re
if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', "user@gmail.com"):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$', "https://www.python.org"):
    print("Valid URL")
else:
    print("Invalid URL")
