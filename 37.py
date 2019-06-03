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

def is_prime(number):
    if number in {0,1}:
        return False
    elif number in {2,3}:
        return True
    
    for x in range(2,int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

def prime_gen(cap):
    #yield 2
    
    i = 11#3
    while i < cap:
        if is_prime(i):
            yield i
        i += 2

#generates truncated numbers first from left to right (1234 -> 123 -> 12 -> 1)
#then from right to left (1234 -> 234 -> 34 -> 4)
def trunc_gen(num):
    num = str(num)
    Len = len(num)
    
    for i in range(1,Len):
        yield int(num[i:Len])
    for i in range(Len,1,-1):
        yield int(num[0:i - 1])

@dect
def main():
    l = []
    for prime in prime_gen(10**10):
        if any({x in str(prime) for x in ("4","6","8","0")}):
            continue
        flag = 0
        for trunc in trunc_gen(prime):
            if not is_prime(trunc):
                flag = 1
                break
        if flag == 0:
            l.append(prime)
            print(prime)
        if len(l) == 11:
            break
    print("{}: {}\n#primes: {}".format(l,sum(l),len(l)))
        
main()