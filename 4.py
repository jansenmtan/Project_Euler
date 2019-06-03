#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def palindrome_checker(num):
    number = str(num)
    rebmun = reversed(number)
    
    if list(number) == list(rebmun):
        return True
    else:
        return False
        
TD = [item
      for item in range(900,1000)]

TDR = 100
C0 = [item
      for item in range(100)]
C1 = [item
      for item in range(100)]
i0 = 0
palindrome_list = []

for i1 in C1:
    if i1 % TDR == 0:
        del C1[0]
        TDR -= 1
        i0 += 1
        if len(C1) == 0:
            break

    #print(C1[:5])
    print("{}: {} × {} = {}".format(i1,
    	                               TD[C0[i0]],
                                    TD[C1[(i1 - i0) % TDR]],
                                    TD[C0[i0]] * TD[C1[(i1 - i0) % TDR]]))

    if palindrome_checker(TD[C0[i0]] * TD[C1[(i1 - i0) % TDR]]) == True:
        palindrome_list.append(TD[C0[i0]] * TD[C1[(i1 - i0) % TDR]])    
    
print(max(palindrome_list))