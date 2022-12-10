#file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
file = open('input.txt', 'r', encoding='utf-8').read().splitlines()

aaaaaa, bbbbbb = [1], []
for i in file:
    inp = i.split()
    if len(inp) == 1:
        aaaaaa.append(aaaaaa[-1])
    else:
        aaaaaa.append(aaaaaa[-1])
        aaaaaa.append(aaaaaa[-1] + int(inp[1]))

print(sum(map(lambda q: aaaaaa[q-1] * q, list(range(20, 220 + 1, 40)))))

for i in range(241):
    bbbbbb.append('#' if abs((i % 40) - aaaaaa[i]) <= 1 else '.')

lines = list(map(lambda q: ''.join(bbbbbb[q:q+40]), range(0, 200 + 1, 40)))
print('\n'.join(lines))
