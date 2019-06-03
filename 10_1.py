#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
"""This implementation inspired (stolen from) Idconejo"""

def is_prime(unsub,prime_list):
    for prime in prime_list:
        if prime > int(unsub ** 0.5 + 1):
            break
        if unsub % prime == 0:
            return False
    return True

def prime_summer(cap):
    known_primes = [2]
    Sum = 2
    
    for unsub in range(3,cap):
        if is_prime(unsub,known_primes) == True:
            Sum += unsub
            known_primes.append(unsub)
    
    return Sum

s = time.time()
print("{}\n{} s".format(prime_summer(2000000),time.time() - s))

"""This implementation is slower because of lists"""