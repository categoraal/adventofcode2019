input = [int(i) for i in open('day4\input4').read().strip().split('-')]

a = input[0]
b = input[1]
count = 0

while a < b:
    ns = str(a)
    if ns[0] <= ns[1] and ns[1] <= ns[2] and ns[2] <= ns[3] and ns[3] <= ns[4] and ns[4] <= ns[5]:
        if ns[0] == ns[1] or ns[1] == ns[2] or ns[2] == ns[3] or ns[3] == ns[4] or ns[4] == ns[5]:
            count += 1
    a += 1

print(count)