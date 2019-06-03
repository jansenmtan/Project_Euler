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


def is_palindrome(num):
    number = str(num)
    rebmun = reversed(number)
    
    return list(number) == list(rebmun)

@dect
def main():      
    biggest_palindrome = 0
    
    for x in range(900,1000):
        for y in range(900 + (900 - x),1000):
            x_y = x * y
            if is_palindrome(x_y) and (x_y > biggest_palindrome):
                biggest_palindrome = x_y
    
    print(biggest_palindrome)

main()
