from Intcode import computer
from collections import defaultdict
data = open('11').read().strip().split(',')
it = [int(i) for i in data]
ins = defaultdict(lambda:0)
for idx,val in enumerate(it):
    ins[idx] = val

dr = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
dl = {(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1),(0,1):(-1,0)}

route = [(0,0)]
colormap = defaultdict(lambda:0)
dir = (-1,0)
ptr = 0
base = 0
for y,x in route:
    color = colormap[(y,x)]
    paint, ptr,base = computer(ins,[color],feedback=True,ptr=ptr,base=base)
    if paint == 'b':
        break
    nd, ptr,base = computer(ins,[],feedback=True,ptr=ptr,base=base)
    if nd == 'b':
        break
    paint = paint[0]
    nd = nd[0] 
    colormap[(y,x)] = paint
    if nd == 1:
        dir = dr[dir]
        dy,dx = dir
        route.append((y+dy,x+dx))
    if nd == 0:
        dir = dl[dir]
        dy,dx = dir
        route.append((y+dy,x+dx))

print(len(set(route)))

it = [int(i) for i in data]
ins = defaultdict(lambda:0)
for idx,val in enumerate(it):
    ins[idx] = val

route = [(0,0)]
colormap = defaultdict(lambda:0)
colormap[(0,0)] = 1
dir = (-1,0)
ptr = 0
cnt =0
base = 0
for y,x in route:
    cnt += 1
    color = colormap[(y,x)]
    paint, ptr,base = computer(ins,[color],feedback=True,ptr=ptr,base=base)
    if paint == 'b':
        break
    nd, ptr,base = computer(ins,[],feedback=True,ptr=ptr,base=base)
    if nd == 'b':
        break
    paint = paint[0]
    nd = nd[0] 
    colormap[(y,x)] = paint
    if nd == 1:
        dir = dr[dir]
        dy,dx = dir
        route.append((y+dy,x+dx))
    if nd == 0:
        dir = dl[dir]
        dy,dx = dir
        route.append((y+dy,x+dx))


ys=[];xs=[]
for i in colormap:
    y,x = i
    ys.append(y)
    xs.append(x)

for y in range(max(ys)+1):
    line = ''
    for x in range(max(xs)+1):
        if colormap[(y,x)] == 1:
            line += '#'
        else:
            line += ' '
    print(line)