#Question 3
Str_1 = "Harshada"
Str_2 = "Akshata"
print(Str_1[:2])
print(Str_1[:])
print("Concatanation of string")
print(Str_1 + Str_2)

duplicate = []
for i in Str_1:
    count = Str_1.count(i)
    if Str_1.count(i):
        print(f"{i} : {count}")
        duplicate.append(i)
        