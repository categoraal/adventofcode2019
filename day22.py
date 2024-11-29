data = open('22').read().strip().split('\n')

N = 10007#number of cards

coef = []
for l in data:
    sp = l.split(' ')
    if l.startswith('deal into new'):a,b = (-1,-1)
    if l.startswith('cut'):a,b = (1,-int(sp[-1]))
    if l.startswith('deal with increment'):a,b = (int(sp[-1]),0)
    coef.append((a,b))

def compose(l:list):
    a,b = l[0]
    for i in l[1:]:
        c,d = i
        e = a*c
        f = c*b+d
        a,b=e,f
    return a,b

a,b = compose(coef)
print((a%N*2019+b%N)%N)
#part 2
N = 119315717514047 #number of cards
times = 101741582076661
a = a%N;b=b%N

functionSeries = [(a,b)]
while len(functionSeries) < 47:
    na,nb = compose(2*[functionSeries[-1]])
    na = na%N
    nb = nb%N
    functionSeries.append((na,nb))

ncoef = []
for l,r in zip(functionSeries,bin(times)[2:][::-1]):
    if r == '1':
        ncoef.append(l)
n = 0
for i,val in enumerate(bin(times)[2:][::-1]):
    n += int(val)*(2**i)

a,b = compose(ncoef)
a=a%N;b=b%N
a_inv = pow(a,-1,N)
x = a_inv*(2020-b)%N
print(x)