#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
from math import log10
from math import factorial

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

def factchecker(number):
    copy = number
    n_len = int(log10(number))
    Sum = 0
    
    for exp in range(n_len,-1,-1):
        digit = number // 10**exp
        Sum += factorial(digit)
        number -= (digit * 10**exp)
    
    if Sum == copy:
        return True
    else:
        return False

@dect
def main():
    Sum = 0
    for num in range(10,40730):
        if factchecker(num):
            Sum += num
    print(Sum)
main()