#-*-coding:utf8;-*-
#qpy:3
#qpy:console
'''Thanks Stack Overflow!'''
def factorizer(number,limit):
    factors = []
    gate = isinstance(limit,int)
    
    for x in range(1,int(number ** 0.5) + 1):
        
        '''if x % round(number / 100) == 0:
            print("Iteration: {}".format(x))'''
            
        if number % x == 0:
            factors.append(x)
            if x != int(number / x):
                factors.append(int(number / x))
            if gate == True:
                if len(factors) > limit:
                    break
    
    factors.sort()
    return factors

def is_abundant(number):
    number_factors = factorizer(number,"")[:-1]
    
    if sum(number_factors) > number:
        return True
    else:
        return False

abundants = [number
             for number in range(1,28123 + 1)
             if is_abundant(number)]

print("Made abundants")

not_addends = {abundant + bundant
               for abundant in abundants
               for bundant in abundants[abundants.index(abundant):]
               if abundant + bundant < 28123 + 1}

print("Made not addends")

addends = [number
           for number in range(1,28123 + 1)
           if number not in not_addends]

print("Made addends")

print(sum(addends))