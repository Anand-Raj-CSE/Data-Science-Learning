import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i} is: {i*i*i}")

if __name__ == "__main__": 
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t= time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish_time = time.time() - t
    print(finish_time)

