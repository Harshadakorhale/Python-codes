#Multithreading means running multiple threads simultaneously.
#A thread is a small part of a process

import threading
def task():
    print("hello")

Thred1 = threading.Thread(target=task)
Thred1.start()