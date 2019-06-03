#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
from itertools import count

#decorator that gets execution time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

def is_pentagonal(num):
    return ((1 + (1 + 24*num)**0.5)/6) % 1 == 0

def P(n):
    return n*(3*n - 1)/2

def S(n,a):
    return P(n) + P(n + a)

def D(n,a):#i got royalty inside this
    return P(n + a) - P(n)

@dect
def main():
    flag = 0
    for i in count(10):
        for j in count(1):
            if j > 1000:
                print((i,j))
                break
            if is_pentagonal(D(i,j)) and is_pentagonal(S(i,j)):
                min = (D(i,j),S(i,j))
                flag = 1
                break
        if flag == 1:
            break
    print(min)

main()