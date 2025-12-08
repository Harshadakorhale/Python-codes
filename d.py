#Append the content of file 
#if we dont want to remove existing data the append()
a = open("a.txt","a")
b = a.write("welcome")
print()
a.close()