from Intcode import computer
from collections import defaultdict,deque

data = [int(i) for i in open('19').read().strip().split(',')]
def r_ins():
    ins = defaultdict(int)
    for i,v in enumerate(data): ins[i] = v
    return ins


size = 50
kaart = {}
cnt = 0
for y in range(size):
    for x in range(size):
        c = [x,y]
        ins = r_ins()
        r = computer(ins,c,direct=True)
        kaart[(x,y)] = r[0]
        if r[0] == 1:
            cnt+=1

print(cnt)


origin = [6+9,5+8]
queue = deque([tuple(origin)])

dirs = ((1,0),(0,1))
offset = ((-99,99),(99,-99))
kaart = {tuple(origin):1}
flag = False
while True:
    p = queue.popleft()
    if flag:
        break
    x,y = p
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if (nx,ny) not in queue and (nx,ny) not in kaart:
            ins = r_ins() 
            r = computer(ins,[nx,ny],direct=True)[0]
            kaart[(nx,ny)] = r
            if r == 1:
                queue.append((nx,ny))
                for ox,oy in offset:
                    x2,y2 = nx+ox,ny+oy   
                    if (x2,y2) in kaart and kaart[(x2,y2)] == 1:
                        if ox == -99:
                            print((nx+ox)+10000+ny)
                        else:
                            print(nx*10000+ny+oy)
                        flag = True 