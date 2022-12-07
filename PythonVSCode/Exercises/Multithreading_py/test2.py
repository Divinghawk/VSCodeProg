import threading
import time

# Program to check if a number is prime or not

num = 4

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False
def prime(num):
# prime numbers are greater than 1
    if num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break


# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
threading.Thread(target=prime(num)).start()

class MyThread(threading.Thread):
    def run(self):                                         # Default called function with mythread.start()
        print("{} started!".format(self.getName()))        # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))       # "Thread-x finished!"

def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, run method will be invoked
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another

if __name__ == '__main__':
    main()