# 7. Write a Python program to extract all numbers from the string "Order123 has 4 items 
# costing 250 each" using regex.

import re
string1 = "harshada015hello"
number = re.findall(r"\d+",string1)
print(number)
