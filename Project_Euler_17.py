#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def into_word(number):
    ones = {1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            0:"",
            }
    
    teens = {1:"eleven",
             2:"twelve",
             3:"thirteen",
             4:"fourteen",
             5:"fifteen",
             6:"sixteen",
             7:"seventeen",
             8:"eighteen",
             9:"nineteen",
             0:"ten",
             }
    
    tens = {2:"twenty",
            3:"thirty",
            4:"forty",
            5:"fifty",
            6:"sixty",
            7:"seventy",
            8:"eighty",
            9:"ninety",
            0:"",
            }
    
    number = [int(digit)
              for digit in list(reversed(str(number)))]
    
    num = [number[i:i + 3]
           if len(number[i:i + 3]) == 3
           else [number[i],number[i + 1],"×"]
           if len(number[i:i + 3]) == 2
           else [number[i],"×","×"]
           for i in range(0, len(number), 3)]
    num.reverse()
    for i in range(len(num)):
        num[i].reverse()
    
    word = ""
    
    #reads from left to right output is in order and complies with british convention. could be read easily by an english reader (if spaces were added).
    for triplet in range(len(num)):
        for digit in range(3):
            if isinstance(num[triplet][digit],int):
                if digit == 0:
                    word += ones[num[triplet][digit]]
                     
                    
                    if num[triplet][digit] != 0:
                        word += "hundred"
                         
                    
                    if (num[triplet][digit + 1] != 0 or
                        num[triplet][digit + 2] != 0):
                        word += "and"
                        
                elif (digit == 1 and
                      num[triplet][digit] != 1):
                    word += tens[num[triplet][digit]]
                     

                elif digit == 2:
                    if num[triplet][digit - 1] == 1:
                        word += teens[num[triplet][digit]]
                         

                    else:
                        word += ones[num[triplet][digit]]
                         
                    
                    if (triplet < 1 and
                        len(num) > 1):
                        word += "thousand"
                         


                
    
    return word

Sum = sum([len(into_word(n))
           for n in range(1,1001)])

print(Sum)