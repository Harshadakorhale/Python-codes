# 8. Write a program to display even numbers between 1 to 50 using a for loop. 

even = []
for i in range(1,51):
    if i % 2 == 0:
        even.append(i)
print(even)
