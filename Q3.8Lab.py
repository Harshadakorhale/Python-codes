# 8. Write a Python program using the threading module to create two threads: 
#  Thread 1 prints numbers from 1–5 
#  Thread 2 prints numbers from 6–10

import threading
def task1():
    for i in range(1,6):
      print(i)
Thred1 = threading.Thread(target=task1)
Thred1.start()

def task2():
   for x in range(6,11):
      print(x)
Thred2 = threading.Thread(target=task2)
Thred2.start()

