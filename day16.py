data = open('16').read().strip()

def phase(l):
    res = [] 
    for i in range(len(data)):
        n = 0
        if i > len(data)/2:
            n = sum(data[i:])
        else:
            for j,k in enumerate(l):
                n += ([0,1,0,-1][((j+1)//(i+1))%4])*k
        res.append(abs(n)%10)
    return res

data = [int(i) for i in data]
for _ in range(100):
    data = phase(data)

print(''.join([str(i) for i in data[:8]]))

data = open('16').read().strip()*10000
offset = int(data[:7])
data = [int(i) for i in data[offset:]]

for i in range(100):
    nd = []
    value = 0
    for _,val in enumerate(data[::-1]):
        value += val
        nd.append(value%10)
    data = nd[::-1]
print(''.join([str(i) for i in data[:8]]))