#write File 
#Content is overriden by using write()

a = open("a.txt","w")
b = a.write("Harshu")
print(b)
a.close()