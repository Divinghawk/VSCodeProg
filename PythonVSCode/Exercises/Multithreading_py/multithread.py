from threading import Thread
import time
# Program to check if a number is prime or not
# Real Prime-List: 2, 17, 181, 3801247, 8005343, 14612209, 309490229, 885847591, 982451653, 9000004879
num = 9000003783
# Keine Primzahlen: 1, 11179, 200871, 3001589, 50000241, 800002197, 9000003783
#numlist= [1, 11179, 200871, 3001589, 50000241, 800002197, 9000003783]
def prime(num):
    if num > 1:
        # check factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, 'not a prime number')
                break
        else:
            print(num, 'is a prime number')
    # is input number less than or equal to 1, it is not a prime
    else:
        print(num, 'is not a prime number, less or equal than 1')
 
 
if __name__ == "__main__":
    start_time=time.perf_counter()
    threads = []
    # Anzahl der Threads wählen
    num_threads = 1
    
    # create threads
    for i in range (num_threads):
        thread = Thread(target=prime(num))
        threads.append(thread)
    
    # start threads
    for thread in threads:
        thread.start()
    
    # join threads: wait for them to complete
    for thread in threads:
        thread.join()
    
    print('end main thread')
    #end time
    end_time=time.perf_counter()
    print(f"Total time of Threading execution {round(end_time- start_time,4)} for the function ")
