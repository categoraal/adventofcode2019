data = open('2').read().split(',')
data = [int(i) for i in data]
data[1] = 12
data[2] = 2
print(data,'\n')
for i, val in enumerate(data):
    if i%4 == 0:
        if val == 1:
            a = data[i+1]
            b = data[i+2]

            position = data[i+3]
            data[position] = data[a] + data[b]
        if val == 2:
            a = data[i+1]
            b = data[i+2]
            position = data[i+3]
            data[position] = data[a] * data[b]
        if val == 99:
            break
        print(data,'\n')

print(data[0], '\n')