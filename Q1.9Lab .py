# 9. Write a program to find the sum of digits of a number using while loop. 

number = 111
sum_digits = 0

n = number
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(sum_digits)