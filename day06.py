data = open('6').read().strip().split('\n')

graph = {}
for line in data:
    s,o = line.split(')')
    if s in graph:
        graph[s].append(o)
    else:
        graph[s] = [o]

start = 'COM'
orbits = 0
sf = True
sy = True
paths = {}
def recursion(start,orbits,path,sf,sy):
    res = 0
    if start in graph:
        for i in graph[start]:
            res += recursion(i,orbits+1,path|{i},sy,sf)
            if i =='SAN' and sf:
                paths['SAN'] = path|{'SAN'}             
                sf = False
            if i == 'YOU' and sy:
                paths['you'] = path|{'you'}
                sy = False
    res += orbits
    return res

print(recursion(start,orbits,{'COM'},sy,sf))

p = paths['SAN']&paths['you']
n = len(p)-1
ny = len(paths['you'])-1
ns = len(paths['SAN'])-1
print(ny+ns-n-n-2)