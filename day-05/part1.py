import re

# file = open('test.txt', 'r')
file = open('input.txt', 'r')

arrays = []
input_txt = file.read().split('\n\n')
for line in input_txt[0].split('\n'):
    if line.__contains__(' 1   2'):
        break
    row = re.split('....', line)
    res = [line[i:i + 4] for i in range(0, len(line), 4)]
    row = [x[1] if x[1] != ' ' else '' for x in res]
    arrays.append(row)

new_arr = []
for i in range(0, len(arrays[0])):
    col = []
    for x in arrays[::-1]:
        if x[i] != '':
            col.append(x[i])
    new_arr.append(col)

for line in input_txt[1].split('\n'):
    cmd = list(map(int, re.findall('\d+', line)))
    for i in range(0, cmd[0]):
        p = new_arr[cmd[1] - 1].pop()
        new_arr[cmd[2] - 1].append(p)

msg = ''
for x in new_arr:
    msg = msg + x.pop()
print(msg)
