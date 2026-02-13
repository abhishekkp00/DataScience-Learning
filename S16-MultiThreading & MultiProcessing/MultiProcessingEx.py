import multiprocessing
import time
import sys
import math

#Increase the max number of digits in an integer string to allow for deeper recursion
sys.set_int_max_str_digits(1000000)

def computer_factorial(n):
    print(f'Computing the factorial of {n}')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}')
    return result

if __name__ == "__main__":
    numbers = [1000, 2000, 3000, 4000, 5000]
    
    start_time = time.time()
    
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)
    
    end_time = time.time()
    print(f"Time taken to compute factorials: {end_time - start_time:.2f} seconds")