import string
# file = open('test.txt', 'r')
file = open('input.txt', 'r')
score = 0
for line in file.readlines():
    a, b = line[:len(line)//2], line[len(line)//2:]
    res = [a.count(x) and b.count(x) for x in string.ascii_letters]
    score = score + (res.index(sorted(res)[-1])+1)
print(score)
