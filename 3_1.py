#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#lesson learned: list comprehensions are slow af

num = 600851475143
#num = 37

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

factor_list = list(enumerate(factorizer(num,"uhhhh no limit")))

#print(factor_list)

for i in factor_list:
    if int(num**0.5 + 1) < i[1]:
        cutoff = i[0]
        break
del factor_list[cutoff:]

print([item[1]
       for item in factor_list
       if (len(factorizer(item[1],2)) <= 2) and (item[1] != 1)])