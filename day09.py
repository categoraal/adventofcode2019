from collections import defaultdict
data = open('9').read().split(',')
ins = [int(i) for i in data]


def mode(ptr,para,ins,base):
    # if ptr < 0: print('oeps')
    # if ins[ptr] < 0: print('oeps?')
    if para == '0': return ins[ins[ptr]]  #location
    if para == '1': return ins[ptr] #immediate
    if para == '2': return ins[base+ins[ptr]]#relative

def computer(ins,inout,ptr=0,feedback=False): #inout in reverse order
    base = 0
    res = []
    while ptr < len(ins):
        val = str(ins[ptr]).zfill(5)
        p3,p2,p1,_,_ = [i for i in val]
        if val.endswith('03'): #save
            if len(inout) == 0:
                raise Exception('no input')
            if p1 == '0': ins[ins[ptr+1]] = inout.pop(0)
            if p1 == '2': ins[ins[ptr+1]+base] = inout.pop(0)
            ptr += 2
        elif val.endswith('04'): #output
            # out= ins[ins[ptr+1]]
            out = mode(ptr+1,p1,ins,base)
            ptr += 2
            res.append(out)
            if feedback:
                return out,ptr
            
        elif val.endswith('99'): #break
            return res
        elif val.endswith('09'): #change base
            base += mode(ptr+1,p1,ins,base)
            ptr += 2
        else:
            v1 = mode(ptr+1,p1,ins,base)
            v2 = mode(ptr+2,p2,ins,base)
            if  val.endswith('01'): #add
                if p3 == '0': ins[ins[ptr+3]] = v1 + v2
                if p3 == '2': ins[ins[ptr+3]+base] = v1 + v2
                ptr += 4

            elif val.endswith('02'): #mult
                if p3 == '0':ins[ins[ptr+3]] = v1 * v2
                if p3 == '2': ins[ins[ptr+3]+base] = v1 * v2
                ptr += 4
            elif val.endswith('05'): #jump if true
                ptr = v2 if v1 != 0 else ptr+3
            elif val.endswith('06'): #jump if false
                ptr = v2 if v1 == 0 else ptr+3 
            elif val.endswith('07'): #less than
                if p3 == '0':ins[ins[ptr+3]] = 1 if v1 < v2 else 0 
                if p3 == '2':ins[ins[ptr+3]+base] = 1 if v1 < v2 else 0
                ptr += 4
            elif val.endswith('08'): #equals
                if p3 == '0':ins[ins[ptr+3]] = 1 if v1 == v2 else 0 
                if p3 == '2':ins[ins[ptr+3]+base] = 1 if v1 == v2 else 0 
                ptr += 4  
    print('all instructions completed')
    return res


memory = []
instructions = defaultdict(lambda:0)
for idx, val in enumerate(ins):
    instructions[idx] = val

print(computer(instructions,[1])[0])

instructions = defaultdict(lambda:0)
for idx, val in enumerate(ins):
    instructions[idx] = val

print(computer(instructions,[2])[0])
