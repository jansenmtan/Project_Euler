#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def prime_finder(target_pos):
    unsub = 3
    unsub_pos = 1
    
    while unsub_pos < target_pos:
        limit = int(unsub ** 0.5) + 1
        factor_count = 0
            
        for i in range(1,limit):
            if unsub % i == 0:
                factor_count += 1
                if factor_count > 1:
                    break
        
        if factor_count == 1:
            unsub_pos += 1
            #print("{}: {}".format(unsub_pos,unsub))
            if unsub_pos == target_pos:
                return unsub
        
        unsub += 1
    
print("Result: " + str(prime_finder(10001)))
        