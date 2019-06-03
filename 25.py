#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def fib_gen(f0,f1,count_f1):
    while True:
        yield (f1,count_f1)
        f1 += f0
        f0 = f1 - f0
        count_f1 += 1

for num in fib_gen(0,1,1):
    if len(str(num[0])) == 1000:
        print("{} is the {}th Fibonacci number.".format(num[0],num[1]))
        break
