# 4. Write a Python program that takes a string "Hello World" and uses built-in functions 
#     to count characters, convert to uppercase, and check if it starts with "H". 

str1 = "Hello World"
print("Count of characters is :",len(str1))

ucase = str1.upper()
print("String in Upper case :",ucase)

if str1[0]=='H':
        print("Starts with H")
else:
    print("not starts with H")

      