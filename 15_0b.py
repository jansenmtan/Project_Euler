#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#number counting method: mapping paths to a unique number
#takes forever. cheated and used OEIS to see sequence.
#brute force- combinatorial method is much smarter

for i in range(3,11):     
     l = i #l for length
     board = [0 for i in range(l)]
     
     count = 1
     f = 0 #f for focus
     while board[l - 1 - 2] != l - 1:
          board[f] += 1
          
          #process to carry one
          if board[f] == l:
               f += 1
               
               while board[f] == l - 1: #find rightmost uncarryable number
                    f += 1
               board[f] += 1 #carry
               
               f1 = f #carry all the way to the left
               while f > 0:
                    f -= 1
                    board[f] = board[f1]
          
          count += 1
     
     print(count * 2)
     
