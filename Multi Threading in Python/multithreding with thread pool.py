# Multithreding with thread pool executor
# first we need to import the library which we require


import time
from concurrent.futures import ThreadPoolExecutor

def print_number(number):
    time.sleep(1)
    return f"Number is : {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,11,12,13]
start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)

end_time = time.time() - start_time
print(f"time taken : {end_time}")