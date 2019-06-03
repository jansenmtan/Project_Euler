#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time

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
    Sum = 0
    for unsub in range(10,5 * 9**5):
        u = str(unsub)
        Σ_d = sum([int(digit)**5 for digit in u])
    
        if Σ_d == unsub:
            Sum += unsub
    print(Sum)
main()