# A simple code to explain multithreading
import threading


def print_cube(num):
    print(num ** 3)


def print_square(num):
    print(num ** 2)


t1 = threading.Thread(target=print_cube, args=(10,))  # defining one thread
t2 = threading.Thread(target=print_square, args=(10,)) # defining second thread
t1.start()
t2.start()

# waits until both threads finish their task
t1.join()
t2.join()

print("Done")
