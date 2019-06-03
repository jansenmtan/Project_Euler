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
    prod_n = 1
    prod_d = 1

    for n in range(12,100):
        if n % 10 == 0 or n % 11 == 0:
            continue
        #print("n: {}".format(n))
        for d in range(n,100):
            if any([d == n,
                    d % 10 == 0,
                    d % 11 == 0,]):
                continue
            #print("d: {}".format(d))
            l_n = [digit
                   for digit in str(n)
                   if digit not in set(str(d))]

            l_d = [digit
                   for digit in str(d)
                   if digit not in set(str(n))]
            
            if len(l_n) != 1:
                continue
            
            mut_n = int("".join(l_n))
        
            mut_d = int("".join(l_d))
        
            if mut_n / mut_d == n / d:
                prod_n *= mut_n
                prod_d *= mut_d

    print("{} / {}".format(prod_n,prod_d))

main()