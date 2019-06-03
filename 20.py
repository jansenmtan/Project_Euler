#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def factorial(number):
    factors = [number - i for i in range(number)]
    
    product = 1
    for factor in factors:
        product *= factor
    
    return product

print(sum([int(digit) for digit in list(str(factorial(100)))]))