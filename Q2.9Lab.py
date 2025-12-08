# 9. Write a program to read a file "data.txt" and display its content. Implement proper 
# exception handling for: 
#  File not found 
#  Permission errors 
#  Any other I/O errors 
# Print appropriate messages for each case.

import fileinput
filename = "data.txt"
try:
    print("File content :\n")
    for line in fileinput.input(files=filename):
        print(line,end="")
except FileNotFoundError:
    print("The file 'data.txt' was not found")
except PermissionError:
    print("You dont have permission to read 'data.txt' file")
except IOError:
    print("An IOERROR occurd while reading 'data.txt' file ")
except Exception as e:
    print(f"Unexpected error : {e}")
