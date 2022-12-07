from multiprocessing import Pool
import time
# Liste der zu überprüfenden Prime numbers
# Real Prime-List: 2, 17, 181, 3801247, 8005343, 14612209, 309490229, 885847591, 982451653, 9000004879
numlist = [2, 17, 181, 3801247, 8005343, 14612209, 309490229, 885847591, 982451653, 9000004879]

# Keine Primzahlen: 1, 11179, 200871, 3001589, 50000241, 800002197, 9000003783
#numlist= [1, 11179, 200871, 3001589, 50000241, 800002197, 9000003783]

# Test ob es sich um eine PrimeNumber handelt
def is_prime(number):
    if number == 2 or number == 3:
        return number, True
    if number % 2 == 0 or number < 2:
        return number, False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return number, False
    return number, True

# Übernimmt zu prüfende Nummern und übergibt diese in den Process-Pool
if __name__ == '__main__':
    start_time=time.perf_counter()
    numbers = numlist
    # Anzahl der Prozesse wählen
    pool = Pool(processes=16)
    # Print Pool der Prime
    print(pool.map(is_prime, numbers))
    #end time
    end_time=time.perf_counter()
    print(f"Total time of Process execution {round(end_time- start_time,4)} for the function ")