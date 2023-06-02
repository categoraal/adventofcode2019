input = [int(i) for i in open('day5\input5').read().strip().split(',')]

# 0 is posistion (parameter as an adress)
# 1 is immediate (paramater as a value)

inout = 1
pointer = 0
res = []

for i, val in enumerate(input):
    if i == pointer:
        # print(val,i)
        if int(str(val)[-1]) == 1: #addition
            
            instruction = str(val).zfill(5)
            # param 1
            if instruction[2] == '0': 
                a = input[input[i+1]]
            else:
                a = input[i+1]
                
            # param 2
            if instruction[1] == '0':
                b = input[input[i+2]]
            else:
                b = input[i+2]


            position = input[i+3]
            input[position] = a+b
            pointer += 4

        if int(str(val)[-1]) == 2: #multiply
            instruction = str(val).zfill(5)
            # param 1
            if instruction[2] == '0': 
                a = input[input[i+1]]
            else:
                a = input[i+1]
                
            # param 2
            if instruction[1] == '0':
                b = input[input[i+2]]
            else:
                b = input[i+2]

            position = input[i+3]
            input[position] = a*b
            pointer += 4

        if int(str(val)[-1]) == 3: #input
            pointer += 2
            input[input[i+1]] = inout

        if int(str(val)[-1]) == 4: #output
            pointer += 2
            address = input[i+1]
            inout = input[address]
            res.append(inout)
        




        if val == 99: #break the program
            break
        
print(res)
print("the result is:",res[-1])