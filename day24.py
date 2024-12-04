data = open('24').read().split('\n')

def step(x):
    res = []
    ds = ((1,0),(-1,0),(0,1),(0,-1))
    for r in range(len(x)):
        l = ''
        for c in range(len(x[0])):
            tl = x[r][c]
            cnt = 0
            for dr,dc in ds:
                nr,nc = r+dr,c+dc
                if 0 <= nr < 5 and 0 <= nc < 5:
                    if x[nr][nc] == '#':
                        cnt += 1
            if tl == '.' and cnt in (1,2): l+='#'
            elif tl == '.' and cnt in (0,3,4): l+='.'
            elif tl == '#' and cnt == 1: l+='#'
            elif tl == '#' and cnt != 1: l+='.'
        res.append(l)
    return tuple(res)

data = tuple(data)
boards = set() 

while data not in boards:
    boards.add(data)
    data = step(data) 

power = 1
p1 = 0
for i in data:
    for j in i:
        if j == '#':
            p1 += power
        power *= 2   
print(p1)

#part 2 
from collections import defaultdict
data = open('24').read().split('\n')
kaart = {}
for r,v in enumerate(data):
    for c,v2 in enumerate(v):
        if r == c == 2:continue
        kaart[(r,c)] = v2
levels = {0:kaart}

def levelstep(level):
    if level not in levels:
        grid = defaultdict(lambda:'.')
    else:
        grid = levels[level]
    newgrid = defaultdict(lambda:'.')
    ds = ((1,0),(-1,0),(0,1),(0,-1))
    for r in range(5):
        for c in range(5):
            if r == c == 2:continue
            tl = grid[(r,c)]
            cnt = 0
            for dr,dc in ds:
                nr,nc = r+dr,c+dc
                if 0 <= nr < 5 and 0 <= nc < 5 and (nr,nc) != (2,2):
                    if grid[(nr,nc)] == '#':
                        cnt += 1
                if (nr,nc) == (2,2):
                    if level-1 in levels: #inner level
                        if dr == 1:
                            for i in range(5):
                                if levels[level-1][(0,i)] ==  '#':cnt += 1
                        if dr == -1:
                            for i in range(5):
                                if levels[level-1][(4,i)] ==  '#':cnt += 1
                        if dc == -1:
                            for i in range(5):
                                if levels[level-1][(i,4)] ==  '#':cnt += 1
                        if dc == 1:
                            for i in range(5):
                                if levels[level-1][(i,0)] == '#':cnt += 1 

                else:
                    if level+1 in levels: #higher level
                        if nr == 5:
                            if levels[level+1][(3,2)] == '#':cnt += 1
                        if nr == -1:
                            if levels[level+1][(1,2)]== '#':cnt += 1
                        if nc == 5:
                            if levels[level+1][(2,3)]== '#':cnt += 1
                        if nc == -1:
                            if levels[level+1][(2,1)]== '#':cnt += 1
            if tl == '.' and cnt in (1,2): newgrid[(r,c)]='#'
            elif tl == '.' and cnt in (0,3,4): newgrid[(r,c)]='.'
            elif tl == '#' and cnt == 1: newgrid[(r,c)]='#'
            elif tl == '#' and cnt != 1: newgrid[(r,c)]='.'
            newgrid[(2,2)] = '.'
    return newgrid

def minute(levels):
    newlevels = {}
    lower = min(levels)
    upper = max(levels)
    for i in range(lower-1,upper+2):
        grid = levelstep(i)
        newlevels[i] = grid 
    return newlevels

for i in range(200):
    levels = minute(levels)

p2 = 0
for i in levels:
    for key in levels[i]:
        if levels[i][key] == '#':
            p2 += 1
print(p2)