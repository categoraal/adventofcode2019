import copy
input = open('day3\input3').read().strip().split('\n')
input1 = input[0].split(',')
input2 = input[1].split(',')
print(input1[0])
start = [0,0]
path1 = [start]
path2 = [start]

def listgen(instructions, path):
    for i in instructions:
        #print(i)
        dist = int(i[1:])
        match i[0]:
            case 'R':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[0] += 1
                    path.append(a)
            case 'L':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[0] -= 1
                    path.append(a)
            case 'U':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[1] += 1
                    path.append(a)
            case 'D':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[1] -= 1
                    path.append(a)
    print('\n')

listgen(input1,path1)
listgen(input2,path2)
res1 = [tuple(i) for i in path1]
res2 = [tuple(i) for i in path2]

overlapping = list(set(res1) & set(res2))

#print(overlapping)
distances = []
for i in overlapping:
    distances.append(abs(i[0])+abs(i[1]))
print(distances)

print(sorted(distances)[1])

intersection1,intersection2 = [],[]
steps1,steps2 = [],[]

def distancesgen(instructions, path,intersection,steps):
    count = 0
    for i in instructions:
        #print(i)
        dist = int(i[1:])
        match i[0]:
            case 'R':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[0] += 1
                    path.append(a)
                    count+=1

                    if tuple(a) in overlapping:
                        #print('test')
                        intersection.append(a)
                        steps.append(count)
            case 'L':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[0] -= 1
                    path.append(a)
                    count+=1
                    if tuple(a) in overlapping:
                        #print('test')
                        intersection.append(a)
                        steps.append(count)
            case 'U':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[1] += 1
                    path.append(a)
                    count+=1
                    if tuple(a) in overlapping:
                        #print('test')
                        intersection.append(a)
                        steps.append(count)
            case 'D':
                for i in range(dist):
                    a = copy.deepcopy(path[-1])
                    a[1] -= 1
                    path.append(a)
                    count+=1
                    if tuple(a) in overlapping:
                        #print('test')
                        intersection.append(a)
                        steps.append(count)
        
        

    print(count)

path1 = [[0,0]]
path2 = [[0,0]]
distancesgen(input1,path1,intersection1,steps1)
distancesgen(input2,path2,intersection2,steps2)
# print(type(overlapping[0]))
print(steps1,steps2,intersection1,intersection2)

results = []
for i,val in enumerate(intersection1):
    index = intersection2.index(val)
    results.append(steps1[i]+steps2[index])

print(sorted(results))
