import multiprocessing
import time

num = 309490229
def prime(num):
    if num > 1:
        # check factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, 'not a prime numer')
                break
        else:
            print(num, 'is a prime number')
    # is input number less than or equal to 1, it is not a prime
    else:
        print(num, 'is not a prime number, less or equal than 1')
 
def main():
    start_time=time.perf_counter()
    processes = []
    num_processes = 2
    
        # create processes
    for i in range (num_processes):
        process = multiprocessing.Process(target=prime(num))
        processes.append(process)
    
    # start processes
    for process in processes:
        process.start()
    
    # join processes: wait for them to complete
    for process in processes:
        process.join()
    end_time=time.perf_counter()
    

    print("Threads:", num_processes)
    print(f"Total time of Process execution {round(end_time- start_time,4)} for the function ")
    print('end main process')