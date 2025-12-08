# mobno = input("Enter mob no:")
# if len(mobno) == 10 and mobno.isdigit():
#     print("Valid mob no")
# else:
#     print("Enter valid mob no")
    
# # mailid = input("Enter mail id:")
# # print(mailid)



# import re
# phoneno = input("Enter")
# if re.match(r"\d{10}$",phoneno):
#     print("No is valid")
# else:
#     print("no is not valid") 


import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
# Test
emails = ["test@example.com", "user.name@domain.co.in", "invalid@domain", "abcgmail.com"]

for e in emails:
    print(e, "=>", is_valid_email(e))
