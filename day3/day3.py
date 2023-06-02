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
        print(i)
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
# print(path1)
# print(len(path1))
# for i in path1:
#    if i in path2:
#        overlapping.append(i)

# print(len(overlapping))
# res = []
# for i in overlapping:
#     res.append(i[0] + i[1])
    
# res1 = sorted(res)
# print(res1[:3])

overlapping = list(set(res1) & set(res2))

#print(overlapping)
distances = []
for i in overlapping:
    distances.append(abs(i[0])+abs(i[1]))
print(distances)

print(sorted(distances)[1])
