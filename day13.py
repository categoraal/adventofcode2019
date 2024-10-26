from collections import defaultdict
from Intcode import computer
data = open('13').read().strip().split(',')
ins = defaultdict(lambda:0)
for k,v in enumerate(data):ins[k] = int(v)


def run(ins,inout=[]):
    screen = {}
    ptr = base = 0
    while True:
        x,ptr,base = computer(ins,inout,ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        y,ptr,base = computer(ins,[],ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        t,ptr,base = computer(ins,[],ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        if 'b' in [x,y,t,ptr]: break
        screen[(x,y)] = t
    return screen
        
screen = run(ins)
# print(screen)

ans = 0
for key in screen:
    if screen[key] == 2:
        ans += 1

xs = [];ys=[]
for x,y in screen:
    xs.append(x);ys.append(y)

def draw(screen):
    for i in range(max(ys)+1):
        line = ''
        for j in range(max(xs)+1):
            c = str(screen[(j,i)])
            if c == '2':c='.'
            if c == '4':c='@'
            if c == '1':c='#'
            if c == '0':c=' '
            line += c
        print(line)
# draw(screen)
print(ans)
# part 2

def run(ins,inout=[]):
    screen = {}
    ptr = base = 0
    px=bx=0
    while True:
        x,ptr,base = computer(ins,inout,ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        y,ptr,base = computer(ins,[],ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        t,ptr,base = computer(ins,[],ptr=ptr,direct=True,base=base)
        if ptr == 'b':break
        if 'b' in [x,y,t,ptr]: break
        if t == 4: bx = x
        if t == 3: px = x
        if bx > px: inout = [1]
        if bx == px: inout = [0]
        if bx < px: inout = [-1]
        screen[(x,y)] = t
    return screen,base

def draw(screen):
    for i in range(max(ys)+1):
        line = ''
        for j in range(max(xs)+1):
            c = str(screen[(j,i)])
            if c == '2':c='.'
            if c == '4':c='@'
            if c == '1':c='#'
            if c == '0':c=' '
            line += c
        print(line)
        

ins = defaultdict(lambda:0)
for k,v in enumerate(data):ins[k] = int(v)
ins[0] = 2

screen,_ = run(ins,inout=[])
# draw(screen)
print(screen[(-1,0)])