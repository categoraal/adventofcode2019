d = [int(i) for i in open('1').read().split('\n')]
r1=r2=0
for i in d:
    r1 += i//3-2
    while i > 0:
        i = i//3-2
        if i > 0:
            r2 += i
print(r1,r2)