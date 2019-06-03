#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
def prime_summer(cap):
    #unsub = 3
    Sum = 2
    
    for unsub in range(3,cap):
        limit = int(unsub ** 0.5) + 1
        factor_count = 0
            
        for i in range(1,limit):
            if unsub % i == 0:
                factor_count += 1
                if factor_count > 1:
                    break
        
        if factor_count == 1:
            Sum += unsub
            #print("{} => {}".format(unsub, Sum))
        
        #unsub += 1
    return Sum

s = time.time()
print("{}\n{} s".format(prime_summer(200000),time.time() - s))
