# Multiprocessing with Processpoolexecutor

import time
from concurrent.futures import ProcessPoolExecutor

def square_number(number):
    time.sleep(1)
    return f"Square of {number} is : {number*number}"

numbers = [1,2,3,4,5,6,7,8,9,10,11]

start_time = time.time()

# utilizing Processpoolexecutor
with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(square_number,numbers)

for result in results:
    print(result)

end_time = time.time()-start_time
print(end_time)