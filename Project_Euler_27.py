#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from operator import itemgetter

def factorizer(number,limit):
    a = []
    gate = isinstance(limit,int)
    
    for x in range(1,int(number**0.5 + 1)):
        
        '''if x % round(number / 100) == 0:
            print("Iteration: {}".format(x))'''
            
        if number % x == 0:
            a.append(x)
            a.append(int(number / x))
            if gate == True:
                if len(a) > limit:
                    break
    
    a.sort()
    return a

def is_prime(number):
    if number == 0 or number == 1:
        return False
    if len(factorizer(number,2)) > 2:
        return False
    else:
        return True

q_list = []
for a in range(-999,-2):
    for b in range(2,1001):
        #first condition checks when n is zero
        #second condition checks when n is one
        #third condition checks for every odd instance of n
        if any([not is_prime(b),
                a + b < 0,
               (a % 2 == 0 and b % 2 != 0)]):
            continue
        
        #print("{},{}".format(a,b))
        quad_eq = lambda a,b,x: x**2 + a*x + b
        
        n = 0
        while quad_eq(a,b,n) > 0:
            if is_prime(quad_eq(a,b,n)):
                n += 1
            else:
                break
        q_list.append((a,b,n))

Max = max(q_list,key = itemgetter(2))

print("{}: {}".format(Max,Max[0] * Max[1]))