data = open('10').read().strip().split('\n')

asteroids = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':asteroids[(x,y)] = (int(x),int(y)) 


def coef(dx,dy):
    return dx/(abs(dx)+abs(dy)),dy/(abs(dx)+abs(dy))

def sortbyangle(dx,dy,i):
    if dx <= 0 and dy > 0:
        v = abs(dx)/abs(dy)
        q1.append(v)    
        q1d[v] = i
    if dy <= 0 and dx < 0:
        v = abs(dy)/abs(dx)
        q2.append(v)
        q2d[v] = i
    if dx >= 0 and dy < 0:
        v = abs(dx)/abs(dy)
        q3.append(v)
        q3d[v] = i
    if dy >= 0 and dx > 0:
        v = abs(dy)/abs(dx)
        q4.append(v)
        q4d[v] = i


coefficients = {}
for i in asteroids:
    x1,y1 = i
    for j in asteroids:
        x2,y2 = j
        if i != j:
            dx = x1-x2
            dy = y1-y2
            a,b = coef(dx,dy)
            if i in coefficients:
                if (a,b) in coefficients[i]:
                    coefficients[i][(a,b)].append(j)
                else:
                    coefficients[i][(a,b)] = [j]
            else:
                coefficients[i] = {(a,b):[j]}

m = 0
best = (0,0)
for i in coefficients:
    n = len(coefficients[i])
    if n > m:
        m = n
        best = i

q1 = [];q1d = {}
q2 = [];q2d = {} 
q3 = [];q3d = {}
q4 = [];q4d = {}

for a,b in coefficients[best]:
    sortbyangle(a,b,coefficients[best][(a,b)])
inorder = sorted(q1)+sorted(q2)+sorted(q3)+sorted(q4)
print(m)

def rc(d,idx,base):
    # print(idx)
    cnt = 0
    xb,yb = base
    dmin = 1000000
    val = ''

    valmin = 0
    if len(d[idx]) > 0:
        cnt += 1
        for x,y in d[idx]:
            dist = abs(xb-x)+abs(yb-y)
            if dist < dmin:
                dmin = dist
                valmin = (x,y)
        if valmin in d[idx]:
            # print(valmin)
            d[idx].remove(valmin)
    return cnt,valmin

cnt = 0
a200 = ''
while cnt < 200:
    for i in sorted(q1):
        c,v = rc(q1d,i,best)
        cnt += c
        if cnt == 200:
            a200 = v
            break
    for i in sorted(q2):
        c,v = rc(q2d,i,best)
        cnt += c
        if cnt == 200:
            a200 = v
            break
    for i in sorted(q3):
        c,v = rc(q3d,i,best)
        cnt += c
        if cnt == 200:
            a200 = v
            break
    for i in sorted(q4):
        c,v = rc(q4d,i,best)
        cnt += c
        if cnt == 200:
            a200 = v
            break
 
x,y = a200
print(x*100+y)
# print(coefficients[best])
# for i in coefficients[best]:
    # print(coefficients[best][i])
