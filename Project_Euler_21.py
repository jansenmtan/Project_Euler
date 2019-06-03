#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def factorizer(number,limit):
    factors = []
    Range = number
    gate = isinstance(limit,int)
    
    x = 1
    while x < Range:
        
        '''if x % round(number / 100) == 0:
            print("Iteration: {}".format(x))'''
            
        if number % x == 0:
            factors.append(x)
            factors.append(int(number / x))
            Range = int(number / x)
            if gate == True:
                if len(factors) > limit:
                    break
        x += 1
    
    factors.sort()
    return factors

def is_amicable(number):
    number_factors = factorizer(number,"")[:-1]
    
    mate = sum(number_factors)
    
    mate_factors = factorizer(mate,"")[:-1]
    
    if (sum(mate_factors) == number and
        number != mate):
        return [number,mate]
    else:
        return [False]

amicables = [is_amicable(number)[0]
             for number in range(1,10000)
             if not isinstance(is_amicable(number)[0],bool)]

print(amicables)
print(sum(amicables))