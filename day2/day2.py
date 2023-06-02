input = open('input2').read().split(',')
input = [int(i) for i in input]
input[1] = 12
input[2] = 2
print(input,'\n')
for i, val in enumerate(input):
    if i%4 == 0:
        if val == 1:
            a = input[i+1]
            b = input[i+2]

            position = input[i+3]
            input[position] = input[a] + input[b]
        if val == 2:
            a = input[i+1]
            b = input[i+2]
            position = input[i+3]
            input[position] = input[a] * input[b]
        if val == 99:
            break
        print(input,'\n')

print(input[0], '\n')