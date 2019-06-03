#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print(sum([integer
           for integer in range(1000)
           if integer % 3 == 0 or
              integer % 5 == 0]))

'''
Could be written as one line but less efficient
than Project Euler 1.py
'''