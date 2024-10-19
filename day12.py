import math
data = open('12').read().strip().split('\n')

moons = {};velocities = {}
for key,val in enumerate(data):
    moons[key] = [int(i.split('=')[-1]) for i in val[1:-1].split(',')] 
    velocities[key] = [0,0,0]

def timestep():
    for moon in moons:
        for moon2 in moons:
            diff = [a-b for a,b in zip(moons[moon],moons[moon2])] 
            v = []
            for i in diff:
                if i > 0: v.append(-1)
                if i == 0: v.append(0)
                if i < 0: v.append(1)
            velocities[moon] = [a+b for a,b in zip(v,velocities[moon])]
    for moon in moons:
        moons[moon] = [a+b for a,b in zip(velocities[moon],moons[moon])]                    

def energy():
    e = 0
    for moon in moons:
        e += sum([abs(i) for i in moons[moon]])*sum([abs(i) for i in velocities[moon]])
    return e

for cnt in range(1000):
    timestep()
print(energy())

#part 2
x = [];vx = [0,0,0,0]
y = [];vy = [0,0,0,0]
z = [];vz = [0,0,0,0]
for val in data:
    a,b,c = [int(i.split('=')[-1]) for i in val[1:-1].split(',')]
    x.append(a);y.append(b);z.append(c) 

def solver(p:list) -> int:
    v = [0,0,0,0]
    cnt = 0
    start = tuple(p+v)
    while True:
        for idx1,val1 in enumerate(p):
            for val2 in p:
                d = val1-val2
                if d > 0: v[idx1] -= 1
                if d == 0: v[idx1] += 0
                if d < 0: v[idx1] += 1
        p = [a+b for a,b in zip(p,v)]
        state = tuple(p+v)
        if state == start:
            return cnt+1
        cnt += 1

r = []
for i in [x,y,z]:
    r.append(solver(i))

print(math.lcm(*r))