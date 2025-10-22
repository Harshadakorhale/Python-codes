number = 111
sum_digits = 0

n = number
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(sum_digits)