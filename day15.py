from Intcode import computer
from collections import defaultdict
from copy import deepcopy

data = open('15').read().strip().split(',')
ins = defaultdict(int)
for key,val in enumerate(data): ins[key] = int(val)

card = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
kaart = defaultdict(str)
kaart[(0,0)] = '.'

def kaartenmaker(x,y,ins,ptr=0,base=0):
    for d in card:
        newins = deepcopy(ins)
        dx,dy = card[d]
        nx = x+dx;ny=y+dy
        if (nx,ny) not in kaart:
            tile,ptr,base = computer(newins,[d],ptr,base,direct=True)
            if tile == 0:
                kaart[(nx,ny)] = '#'
            if tile == 1:
                kaart[(nx,ny)] = '.'
                kaartenmaker(nx,ny,newins,ptr,base)
            if tile == 2:
                kaart[(nx,ny)] = '@'

kaartenmaker(0,0,ins)
ys=[];xs=[]
for i in kaart:
    y,x = i
    ys.append(y)
    xs.append(x)

LOX = ''
for y in range(min(ys),max(ys)+1):
    line = ''
    for x in range(min(xs),max(xs)+1):
        if (y,x) == (0,0):
            line+='@'
            continue
        if kaart[(y,x)] == '#':
            line += '#'
        elif kaart[(y,x)] == '@':
            line += 'O'
            LOX = (y,x)
        else:
            line += ' '
    print(line)

queue = [LOX]
dmap = {LOX:0}
for x,y in queue:
    dist = dmap[(x,y)]
    for d in card:
        dx,dy = card[d]
        nx = x+dx;ny = y+dy
        if (nx,ny) not in queue and kaart[(nx,ny)] != '#':
            queue.append((nx,ny))
            dmap[(nx,ny)] = dist+1

print(dmap[(0,0)])
print(max([dmap[i] for i in dmap]))