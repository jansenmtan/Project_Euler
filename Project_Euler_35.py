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

def factorizer(number,limit):
    f_set = set()
    gate = isinstance(limit,int)
    
    for x in range(1,int(number**0.5) + 1):
        if number % x == 0:
            f_set.add(x)
            f_set.add(int(number / x))
            Range = int(number / x)
            if gate == True:
                if len(f_set) > limit:
                    break
    return list(f_set)

def prime_gen(cap):
    i = 1
    while i < cap:
        i_fs = factorizer(i,2)
        if len(i_fs) == 2:
            yield i
        i += 2

def digit_shifter(num):
    n_len = len(str(num))
    
    if n_len > 1:
        for i in range(1,n_len):
            mut_n_list = [str(num)[i % n_len] for i in range(i,i + n_len)]
            yield int("".join(mut_n_list))
@dect
def main():
    count = 1
    for prime in prime_gen(1 * 10**6): 
        flag = 0
        for shifted in digit_shifter(prime):
            if len(factorizer(shifted,2)) > 2:
                flag = 1
                break
        
        if flag == 0:
            count += 1
    print(count)

main()