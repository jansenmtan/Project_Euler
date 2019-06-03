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
    Sum = sum([num
               for num in range(1,1000000,2)
               if (str(num) == str(num)[::-1] and
                   "{0:b}".format(num) == "{0:b}".format(num)[::-1])])
    print(Sum)
main()