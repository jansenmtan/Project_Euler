#-*-coding:utf8;-*-
#qpy:3
#qpy:console
'''Problem is trivial. If a number is divisible
   by a power of 2, it is divisible by 2.
   likewise with 3, 4, 5, etc.
   Just multiply all the numbers which are the
   greatest power of a prime (ie 2**4) and less
   than 20. It sounds more complicated than it is.
'''
num = 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19

while True:
    if all([#num % 2 == 0,
            #num % 4 == 0,
            #num % 8 == 0,
            num % 16 == 0,
            #num % 3 == 0,
            num % 9 == 0,
            num % 5 == 0,
            num % 7 == 0,
            num % 11 == 0,
            num % 13 == 0,
            num % 17 == 0,
            num % 19 == 0]) == True:
        print(num)
        break
    
    num += 1

'''I guess what this implementation is is a
   shortcut of the "full" method. That being:
   (1) Finding a list of primes under your
       target. 20 in this case.
   (2) Finding the greatest power of those
       primes under your target. For 2, it
       would be 2 ** 4.
   (3) Multiplying the numbers found in (2)
       together.
'''