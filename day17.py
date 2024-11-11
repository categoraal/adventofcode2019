from Intcode import computer
from collections import defaultdict

data = open('17').read().strip().split(',')
# print(data)
ins = defaultdict(lambda:0)
for i,v in enumerate(data): ins[i] = int(v)

res = []
base = 0;ptr=0
# while ptr != 'b':
while True:
    out,ptr,base = computer(ins=ins,inout=[],direct=True,ptr=ptr,base=base)
    if out == 'b':
        break
    res.append(out)
# res = computer(ins=ins,inout=[],onlyres=True)
# print(res)
l = ''
kaart = {}
r=c=0
stratpos = 0
for i in res:
    if i == 35: l += '#';kaart[(r,c)]='#';r+=1 
    if i == 46: l += '.';kaart[(r,c)]='.';r+=1
    if i == 10: print(l);l='';r=0;c+=1
    if i not in [35,46,10]:
        l += chr(int(i)) 
        startpos = (r,c)
        kaart[(r,c)]=chr(int(i));r+=1

intersection = []
for x,y in kaart:
    if kaart[(x,y)] == '#':
        flag = True
        for x1,y1 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if (x1,y1) in kaart:
                if kaart[x1,y1] != '#':
                    flag = False
        if flag:
            intersection.append((x,y))


allignment = 0
for r,c in intersection:
    allignment += r*c

print(allignment)
# part 2

def newdir(r1,c1,r2,c2):
    dd = {(1,0,0,1):'R',
          (1,0,0,-1):'L',
          (0,1,-1,0):'R',
          (0,1,1,0):'L',
          (-1,0,0,-1):'R',
          (-1,0,0,1):'L',
          (0,-1,1,0):'R',
          (0,-1,-1,0):'L'}
    return dd[(r1,c1,r2,c2)]

queue = [startpos]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
lastdir = (1,0)
cnt = 0
pathlengths = []
directions = ['R']
for r,c in queue:
    dr,dc = lastdir
    nr = r+dr;nc = c+dc
    if (nr,nc) in kaart and kaart[(nr,nc)] == '#':
        cnt += 1
        queue.append((nr,nc))
    else:
        pathlengths.append(cnt)
        cnt = 1
        for dr,dc in dirs:
            nr = r+dr;nc = c+dc
            if (nr,nc) in kaart and (nr,nc) not in queue:
                if kaart[(nr,nc)] == '#':
                    queue.append((nr,nc))
                    directions.append(newdir(*lastdir,dr,dc)) 
                    lastdir = (dr,dc)

# print(pathlengths)
# print(directions)
# print(len(pathlengths))
# print(len(directions))
# [print(i) for i in zip(directions,pathlengths)]
#done by hand by looking at the map
route = 'A,A,B,C,B,C,B,C,B,A'
A = 'R,6,L,12,R,6'
B = 'L,12,R,6,L,8,L,12'
C = 'R,12,L,10,L,10'

def gen_input(l:str) -> list: 
    return [ord(i) for i in l] + [10]

ins = defaultdict(lambda:0)
for i,v in enumerate(data): ins[i] = int(v)

ins[0] = 2
inout = gen_input(route)+gen_input(A)+gen_input(B)+gen_input(C)+gen_input('n')
p2 = computer(ins,inout=inout,ptr=0,onlyres=True)
print(p2[-1])