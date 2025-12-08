# 11. Write a Python program using the datetime module to print the current date, 
# current time, and weekday name. 

from datetime import datetime
now = datetime.now()
print("Current Date:", now.date())
print("Current Time:", now.time())
print("Weekday:", now.strftime("%A"))
