#-*-coding:utf8;-*-
#qpy:3
#qpy:console

diags = []
for num in range(3,1001 + 1,2):
    s = num**2
    for i in range(4):
        diags.append(s - i*(num - 1))

print(sum(diags) + 1)