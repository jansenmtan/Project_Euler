#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def sum_squares(From,to):
    result = sum([item ** 2
                  for item in range(From,to + 1)])
    return result
    
def square_sum(From,to):
    result = sum([item
                  for item in range(From,to + 1)]) ** 2
    return result

print(square_sum(1,100) - sum_squares(1,100))