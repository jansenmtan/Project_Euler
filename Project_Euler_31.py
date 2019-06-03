#-*-coding:utf8;-*-
#qpy:3
#qpy:console
total = 200
count = 0
for two_hun in range(1 + 1):
    total -= 200 * two_hun
    
    if total == 0:
        count += 1
        total += 200 * two_hun
        continue
    
    for one_hun in range(2 + 1):
        total -= 100 * one_hun
        
        if total == 0:
            count += 1
            total += 100 * one_hun
            continue
        
        for fifty_p in range(4 + 1):
            total -= 50 * fifty_p
            
            if total == 0:
                count += 1
                total += 50 * fifty_p
                continue
            
            for twenty_p in range(10 + 1):
                total -= 20 * twenty_p
                
                if total == 0:
                    count += 1
                    total += 20 * twenty_p
                    continue
                
                for ten_p in range(20 + 1):
                    total -= 10 * ten_p
                    
                    if total == 0:
                        count += 1
                        total += 10 * ten_p
                        continue
                    
                    for five_p in range(40 + 1):
                        total -= 5 * five_p
                        
                        if total == 0:
                            count += 1
                            total += 5 * five_p
                            continue
                        
                        for two_p in range(100 + 1):
                            total -= 2 * two_p
                            
                            if total == 0:
                                count += 1
                                total += 2 * two_p
                                continue
                            for one_p in range(200 + 1):
                                total -= 1 * one_p
                                
                                if total == 0:
                                    count += 1
                                    total += 1 * one_p
                                total += 1 * one_p
                            total += 2 * two_p
                        total += 5 * five_p
                    total += 10 * ten_p
                total += 20 * twenty_p
            total += 50 * fifty_p
        total += 100 * one_hun
    total += 200 * two_hun
print(count)