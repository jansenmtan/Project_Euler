#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def sum_digits(number):
    string = list(str(number))
    Sum = sum([int(integer)
               for integer in string])
    return Sum

print(sum_digits(2**1000))