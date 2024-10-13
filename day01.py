import math as m
input = open('input1').read().split('\n')
input = [int(i) for i in input]
print(input[0])
print(type(input[0]))

res = 0
for i in input:
    while i > 0:
        i = m.floor(i/3)-2
        if i > 0:
            res += i
    #res += m.floor(i/3)-2

print(res)