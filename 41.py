#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
from itertools import permutations

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

def is_prime(number):
    if number in {0,1}:
        return False
    elif number in {2,3}:
        return True
    
    for x in range(2,int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

@dect
def main():
    largest = 0
    for n in range(1,8):
        nums = [int("".join(perm)) for perm in list(permutations([str(x) for x in range(1,n + 1)]))]
        for num in nums:
            if is_prime(num) and num > largest:
                largest = num
    print(largest)

main()