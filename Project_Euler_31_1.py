#-*-coding:utf8;-*-
#qpy:3
#qpy:console
"""
Stack Overflow to the rescue for integer partitioning
"""
def coin_asc(total):
    vals = [1,2,5,10,20,50,100,200]
    
def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

partitions = accel_asc(200)
not_wanted = {integer for integer in range(1,201) if integer not in (1,2,5,10,20,50,100,200)}

count = 0
flag = 0
for partition in partitions:
    partition = set(partition)
    for integer in partition:
        if integer in not_wanted:
            flag = 1
            break
    if flag == 0:
        if count % 100 == 0:
            print(partition)
        count += 1
    else:
        flag = 0
print(count)
