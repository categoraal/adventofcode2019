input = open('day6/input6test').read().strip().split('\n')
#print(input)

input = [i.split(')') for i in input]
print(input[0])

start = 'COM'