data = open('20').read().split('\n')

collect = ''
portals = {}
seen = []
for ridx,r in enumerate(data):
    for cidx,c in enumerate(r):
        if (ridx,cidx) not in seen and 65 <= ord(c) <= 90:
            seen.append((ridx,cidx))
            key = c
            if 65 <= ord(data[ridx][cidx+1]) <= 90:
                key += data[ridx][cidx+1]
                seen.append((ridx,cidx+1))
                if 0 <= cidx+2 < len(r) and data[ridx][cidx+2] == '.':
                    coords = (ridx,cidx+2)
                else:
                    coords = (ridx,cidx-1)
            else:
                key += data[ridx+1][cidx]
                seen.append((ridx+1,cidx))
                if 0 <= ridx+2 < len(data) and data[ridx+2][cidx] == '.':
                    coords = (ridx+2,cidx)
                else:
                    coords = (ridx-1,cidx)
            if key in portals:
                portals[key].append(coords)
            else:
                portals[key] = [coords]


jumps = {}
for key in portals:
    if key in 'AAZZ':
        continue
    a,b = portals[key]
    jumps[a] = b;jumps[b] = a

start = portals['AA'][0]
end = portals['ZZ'][0]

dirs = ((1,0),(-1,0),(0,1),(0,-1))

queue = [start]
dkaart = {start:0}
for pos in queue:
    r,c = pos
    d = dkaart[pos]
    if (r,c) in jumps:
        nr,nc = jumps[(r,c)]
        if (nr,nc) not in dkaart:
            dkaart[(nr,nc)] = d+1
            queue.append((nr,nc)) 
        
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc 
        if (nr,nc) == end:
            print(d+1)
            break
        if (nr,nc) not in dkaart and data[nr][nc] == '.':
            queue.append((nr,nc))
            dkaart[(nr,nc)] = d+1
    
#part 2
queue = [(start,0)]
dkaart = {(start,0):0}
breakflag = False
for pos,depth in queue:
    if depth > len(jumps)/2:
        continue
    if breakflag: break
    r,c = pos
    d = dkaart[(pos,depth)]
    if (r,c) in jumps:
        if c == 2 or c == len(data[0])-3 or r == 2 or r == len(data)-3:
            flag = 1
        else: flag = 2
        if flag == 2:
            nr,nc = jumps[(r,c)]
            if ((nr,nc),depth+1) not in dkaart:
                dkaart[((nr,nc),depth+1)] = d+1
                queue.append(((nr,nc),depth+1)) 
        if flag == 1 and depth > 0:
            nr,nc = jumps[(r,c)]
            if ((nr,nc),depth-1) not in dkaart:
                dkaart[((nr,nc),depth-1)] = d+1
                queue.append(((nr,nc),depth-1))
        
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc 
        if (nr,nc) == end and depth == 0:
            print(d+1)
            breakflag = True
            break
        if ((nr,nc),depth) not in dkaart and data[nr][nc] == '.':
            queue.append(((nr,nc),depth))
            dkaart[((nr,nc),depth)] = d+1