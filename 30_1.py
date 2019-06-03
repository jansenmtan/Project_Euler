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
    for x in range(10,5 * 9**5):
        Sum_digits = 0
        
        copy_x = x
        for ten_exp in range(len(str(x)) - 1,-1,-1):
        	divisor = 10 ** ten_exp
        	digit = copy_x // divisor
        	Sum_digits += digit ** 5
        	copy_x -= digit * divisor
        
        if Sum_digits == x:
            Sum += x
    print(Sum)
main()