data = open('7').read().strip().split(',')
ins = [int(i) for i in data]

def computer(ins,inout): #inout in reverse order
    res = []
    ptr = 0
    while ptr < len(ins):
        val = str(ins[ptr]).zfill(5)
        p3,p2,p1,_,_ = [i for i in val]
        if val.endswith('3'): #save
            ins[ins[ptr+1]] = inout.pop()
            ptr += 2
        elif val.endswith('4'): #output
            res.append(ins[ins[ptr+1]])
            ptr += 2
        elif val.endswith('99'): #break
            return res
            break
        else:
            v1 = ins[ins[ptr+1]] if p1 == '0' else ins[ptr+1]
            v2 = ins[ins[ptr+2]] if p2 == '0' else ins[ptr+2]
            if  val.endswith('1'): #add
                ins[ins[ptr+3]] = v1 + v2
                ptr += 4

            elif val.endswith('2'): #mult
                ins[ins[ptr+3]] = v1 * v2
                ptr += 4
            elif val.endswith('5'): #jump if true
                ptr = v2 if v1 != 0 else ptr+3
            elif val.endswith('6'): #jump if false
                ptr = v2 if v1 == 0 else ptr+3 
            elif val.endswith('7'): #less than
                ins[ins[ptr+3]] = 1 if v1 < v2 else 0 
                ptr += 4
            elif val.endswith('8'): #equals
                ins[ins[ptr+3]] = 1 if v1 == v2 else 0 
                ptr += 4



ins = [int(i) for i in data]

computer(ins,[0,3])
maxval = 0
maxsig = []
ll = [0,1,2,3,4]
for i in ll:
    l2 = [n for n in ll if n != i]
    for j in l2:
        l3 = [n for n in l2 if n != j]
        for k in l3:
            l4 = [n for n in l3 if n != k]
            for l in l4:
                l5 = [n for n in l4 if n != l]
                for m in l5:
                    ins = [int(i) for i in data]                    
                    v = computer(ins,[0,i])[-1]
                    ins = [int(i) for i in data]                    
                    v = computer(ins,[v,j])[-1]
                    ins = [int(i) for i in data]                    
                    v = computer(ins,[v,k])[-1]
                    ins = [int(i) for i in data]                    
                    v = computer(ins,[v,l])[-1]
                    ins = [int(i) for i in data]                    
                    v = computer(ins,[v,m])[-1]
                    if v > maxval:
                        maxval = v
                        maxsig = [i,j,k,l,m]

print(maxval)

def computer(ins,inout,ptr=0,feedback=False): #inout in reverse order
    ptr = ptr
    while ptr < len(ins):
        val = str(ins[ptr]).zfill(5)
        p3,p2,p1,_,_ = [i for i in val]
        if val.endswith('3'): #save
            if len(inout) == 0:
                raise Exception('no input')
            ins[ins[ptr+1]] = inout.pop(0)
            ptr += 2
        elif val.endswith('4'): #output
            out= ins[ins[ptr+1]]
            ptr += 2
            if feedback:
                return out,ptr
        elif val.endswith('99'): #break
            return 'b','b'
            break
        else:
            v1 = ins[ins[ptr+1]] if p1 == '0' else ins[ptr+1]
            v2 = ins[ins[ptr+2]] if p2 == '0' else ins[ptr+2]
            if  val.endswith('1'): #add
                ins[ins[ptr+3]] = v1 + v2
                ptr += 4

            elif val.endswith('2'): #mult
                ins[ins[ptr+3]] = v1 * v2
                ptr += 4
            elif val.endswith('5'): #jump if true
                ptr = v2 if v1 != 0 else ptr+3
            elif val.endswith('6'): #jump if false
                ptr = v2 if v1 == 0 else ptr+3 
            elif val.endswith('7'): #less than
                ins[ins[ptr+3]] = 1 if v1 < v2 else 0 
                ptr += 4
            elif val.endswith('8'): #equals
                ins[ins[ptr+3]] = 1 if v1 == v2 else 0 
                ptr += 4  
    print('all instructions completed')
    return [],ptr+2

def combinations(start,stop):
    res = []
    ll = [n for n in range(start,stop+1)]
    for i in ll:
        l2 = [n for n in ll if n != i]
        for j in l2:
            l3 = [n for n in l2 if n != j]
            for k in l3:
                l4 = [n for n in l3 if n != k]
                for l in l4:
                    l5 = [n for n in l4 if n != l]
                    for m in l5:
                        res.append([i,j,k,l,m])
    return res

settings = combinations(5,9)
def loop(setting):
    i,j,k,l,m = setting 
    v = 0
    pa=pb=pc=pd=pe=0
    insA = [int(i) for i in data]                    
    insB = [int(i) for i in data]                    
    insC = [int(i) for i in data]                    
    insD = [int(i) for i in data]                    
    insE = [int(i) for i in data]                    
    in1 = [i,0];in2=[j];in3=[k];in4=[l];in5=[m]
    ve = 0
    while True:
        rest = computer(insA,in1,pa,True)       
        va,pa = rest
        in2.append(va)
        vb,pb= computer(insB,in2,pb,True)
        in3.append(vb)
        vc,pc = computer(insC,in3,pc,True)
        in4.append(vc)
        vd,pd = computer(insD,in4,pd,True)
        in5.append(vd)
        ve,pe = computer(insE,in5,pe,True)
        v = ve if ve != 'b' else v
        if ve == 'b':
            break
        in1.append(ve)
    return v    

res = []
for s in settings:
    res.append(loop(s))

print(max(res))
