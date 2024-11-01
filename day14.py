from collections import defaultdict
data = open('14').read().strip().split('\n')

reactions = {}
for line in data:
    components,out = line.split('=>')
    amount, out = out.split()
    reactions[out] = [int(amount)]
    cs = [];a = []
    for component in components.split(','):
        amount,c = component.strip().split(' ')
        cs.append(c)
        a.append(int(amount))
    reactions[out].append(cs)
    reactions[out].append(a)

def co(nfuel):
    inventory = defaultdict(int)
    inventory['FUEL'] = -nfuel
    ores = 0
    while any([inventory[i] < 0 for i in inventory]):
        for chem in list(inventory.keys()):
            inv = inventory[chem]
            if inv < 0:
                n,components,amounts = reactions[chem]
                mult = -(inv//n)
                inventory[chem] += mult*n
                for comp,amount in zip(components,amounts):
                    if comp == 'ORE':
                        ores += mult*amount 
                    else:
                        inventory[comp] -= mult*amount
    return ores

LIMIT = 1E12 
print(co(1))

def secant(f0,f1):
    x0 = co(f0)
    while f0 != f1:
        x1 = co(f1)
        a = (x1-x0)/(f1-f0)
        b = x0-a*f0
        f2 = (LIMIT-b)//a
        f0,f1 = f1,f2
    return int(f2)

print(secant(1,2))