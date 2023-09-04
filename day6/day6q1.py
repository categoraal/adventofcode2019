input = open('day6/input6').read().strip().split('\n')
#print(input)

input = [i.split(')') for i in input]
input = list(map(list,zip(*input)))
#print(input[0])

start = 'COM'
res = 0

#main loop
def fi(x,ls):
    return [i for i, val in enumerate(ls) if val == x]

print(fi(start,input[0]))

que = input[1][fi(start,input[0])[0]]
print(que)
#print(input)
print(len(input[1]),len(set(input[1])))