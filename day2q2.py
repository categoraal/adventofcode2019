input = open('input2').read().split(',')
input = [int(i) for i in input]

print(input,'\n')

for k in range(100):
    for j in range(100):
        input = open('input2').read().split(',')
        input = [int(i) for i in input]
        i1 = k
        i2 = j
        input[1] = i1
        input[2] = i2
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
                #print(input,'\n')
        if input[0] == 19690720:
            print('the awnser is:', 100*i1+i2)
            break
print(input[0], '\n')