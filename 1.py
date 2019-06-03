#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time

def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

@dect
def main():
    Sum = 0

    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            Sum += i

    print(Sum)

main()