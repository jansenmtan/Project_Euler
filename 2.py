#-*-coding:utf8;-*-
#qpy:3
#qpy:console

fib_seq = [0,1]

while (fib_seq[-1] + fib_seq[-2]) <= 4000000:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

print(sum([item
           for item in fib_seq
           if item % 2 == 0]))
print(fib_seq)