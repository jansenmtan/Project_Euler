#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
from itertools import count
from math import log10

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

@dect
def main():
    d_count = 0
    prod = 1
    for num in count(1):
        for char in str(num):
            d_count += 1
            if log10(d_count) % 1 == 0:
                prod *= int(char)
            if log10(d_count) == 6:
                print(prod)
                return

main()