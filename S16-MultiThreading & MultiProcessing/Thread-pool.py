from concurrent.futures import ThreadPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f'Square {number} * {number} = {number * number}'

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(square_number, numbers)
        for result in results:
            print(result)