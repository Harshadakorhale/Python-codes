try:
    filename = "ab.txt"
    a = open(filename, "w+")
    if filename == "ab.txt":
        x = a.write("Welcome")
        a.seek(0)
        b = a.read(x)
        print("File Content:", b)
    else:
        raise Exception("Filename not found")
    a.close()
except Exception as e:
    print("Not able to find path:", e)


