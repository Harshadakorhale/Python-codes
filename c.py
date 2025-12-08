#write File 
#Content is overriden by using write()

a = open("a.txt","w")
b = a.write("Tanvee")
print(b)
a.close()