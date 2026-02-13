#MultiThreading
import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Numbers: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(2)
        print(f"Letters: {letter}")

t = time.time()
print_numbers()
print_letters()
print(f"Time taken without threading: {time.time() - t:.2f} seconds")