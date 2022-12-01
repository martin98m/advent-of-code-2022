# file1 = open('test.txt', 'r')
file1 = open('input.txt', 'r')
max = 0
sum = 0
while True:
    line = file1.readline()
    if line == '':
        break
    if line == '\n':
        max = max if (max > sum) else sum
        sum = 0
        continue
    sum = sum + int(line)

print(max)