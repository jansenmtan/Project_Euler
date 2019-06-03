#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#num = 600851475143
num = 37

def factorizer(number,limit):
    a = []
    
    Range = [x
             for x in range(1,number + 1)]    
    
    if isinstance(limit,int):
        gate = True
    else:
        gate = False
    
    for x in Range:
        print(x)
        if number % x == 0:
            a.append(int(x))
            print(int(x))
            a.append(int(number / x))
            print(int(number / x))
            del Range[(int(number / x) - 1):]
            if gate == True:
                if len(a) > limit:
                    break
    
    a.sort()
    return a

factor_list = factorizer(num,"uhhhh no limit")

if len(factor_list) <= 4:
    if len(factor_list) == 2:
        print(factor_list[1])
    print(factor_list[2])

else:
    del factor_list[round(len(factor_list) ** 0.5):]

    print([item
           for item in factor_list
           if (len(factorizer(item,2)) <= 2) and (item != 1)])
                