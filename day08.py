data = open('8').read().strip()

WIDTH = 25
HEIGHT = 6
size = WIDTH*HEIGHT
res = {}
display = ['2' for _ in range(size)]
for i in range(int(len(data)/size)):
    layer = data[i*size:(i+1)*size]
    for idx,px in enumerate(layer):
        cpx = display[idx]
        if cpx == '2' and px != '2':
            display[idx]= ' ' if px == '0' else '#'

    res[layer.count('0')] = layer.count('1')*layer.count('2')

print(res[min(res)])

message = ''
for i in range(HEIGHT):
    message += ''.join(display[i*WIDTH:(i+1)*WIDTH])+'\n'
     
print(message)