input = [int(i) for i in open('day5\input5').read().strip().split(',')]

# 0 is posistion (parameter as an adress)
# 1 is immediate (paramater as a value)

inout = 5
pointer = 0
res = []
steps = len(input)
print(steps)

i = 0
while i < steps:
    val = input[i]
    if i == pointer:
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
        
        if int(str(val)[-1]) == 5: #jump-if-true            
            instruction = str(val).zfill(5)
            if instruction[2] == '0': 
                a = input[input[i+1]]
            else:
                a = input[i+1]
                
            if a != 0:
                if instruction[1] == '0':
                    pointer = input[input[i+2]]
                else:
                    pointer = input[i+2]
            else:
                pointer += 3

        if int(str(val)[-1]) == 6: #jump-if-false
            instruction = str(val).zfill(5)
            if instruction[2] == '0': 
                a = input[input[i+1]]
            else:
                a = input[i+1]
                
            if a == 0:
                if instruction[1] == '0':
                    pointer = input[input[i+2]]
                else:
                    pointer = input[i+2]
            else:
                pointer += 3        

        if int(str(val)[-1]) == 7: #less than
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

            if a < b:
                if instruction[0] == '0':
                    input[input[i+3]] = 1
                else:
                    input[i+3] = 1
            else:
                if instruction[0] == '0':
                    input[input[i+3]] = 0
                else:
                    input[i+3] = 0
            pointer += 4

        if int(str(val)[-1]) == 8: #equals
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

            if a == b:
                if instruction[0] == '0':
                    input[input[i+3]] = 1
                else:
                    input[i+3] = 1
            else:
                if instruction[0] == '0':
                    input[input[i+3]] = 0
                else:
                    input[i+3] = 0
                    print()
            pointer += 4                

        if val == 99: #break the program
            break
    i += 1
        
print(res)
print("the result is:",res[-1])