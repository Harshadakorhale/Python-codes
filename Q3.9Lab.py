# 9. Write a program to demonstrate thread synchronization. Use a Lock to prevent two 
# threads from modifying a shared counter at the same time.

import threading
import time

# Shared counter
counter = 0

# Creating a Lock object
lock = threading.Lock()

def increment_counter(thread_name):
    global counter
    for _ in range(5):    # each thread increments 5 times
        lock.acquire()    # acquire the lock before modifying shared data
        try:
            current = counter
            time.sleep(0.1)   # simulate some processing delay
            counter = current + 1
            print(f"{thread_name} incremented counter to {counter}")
        finally:
            lock.release()   # release the lock after done

# Creating threads
t1 = threading.Thread(target=increment_counter, args=("Thread-1",))
t2 = threading.Thread(target=increment_counter, args=("Thread-2",))

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print(f"Final counter value: {counter}")
