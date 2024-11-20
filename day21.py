from Intcode import computer,ASCII
from collections import defaultdict

data = [int(i) for i in open('21').read().strip().split(',')]
ins = defaultdict(int)
for i,v in enumerate(data): ins[i] = int(v)

inout = ASCII('NOT B T')+ASCII('NOT C T')+ASCII('OR D J')+ASCII('AND T J')+ASCII('NOT A T')+ASCII('OR T J')+ASCII('WALK')
r = computer(ins,inout,onlyres=True)
if r[-1] > 1000:
    l = ''.join([chr(i) for i in r[:-1]])
    # print(l)
    print(r[-1])
else:
    l = ''.join([chr(i) for i in r])
    print(l)



ins = defaultdict(int)
for i,v in enumerate(data): ins[i] = int(v)
inout = ASCII('NOT B J')+ASCII('NOT C T')+ASCII('OR T J')+ASCII('AND D J')+ASCII('AND H J')+ASCII('NOT A T')+ASCII('OR T J')+ASCII('RUN')
r = computer(ins,inout,onlyres=True)
if r[-1] > 1000:
    l = ''.join([chr(i) for i in r[:-1]])
    # print(l)
    print(r[-1])
else:
    l = ''.join([chr(i) for i in r])
    print(l)