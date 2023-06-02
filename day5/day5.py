input = [int(i) for i in open('day5\input5').read().strip().split(',')]
print(input,'\n')

# 0 is posistion
# 1 is immediate

inpt = 1
pointer = 0

for i, val in enumerate(input):
    if i == pointer:
        if int(str(val)[-1]) == 1: #addition
            a = input[i+1]
            b = input[i+2]

            position = input[i+3]
            input[position] = input[a] + input[b]
            pointer += 4
        if int(str(val)[-1]) == 2: #multiply
            a = input[i+1]
            b = input[i+2]
            position = input[i+3]
            input[position] = input[a] * input[b]
            pointer += 4
        if val == 3: #input
            pointer += 2
            input[input[i+1]] = inpt
        if val == 4: #output
            pointer += 2
            inpt = input[input[i+1]]
        if val == 99:
            break
        print(inpt,'\n')

print(input[0], '\n')