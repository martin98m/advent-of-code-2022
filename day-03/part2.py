import string
# file = open('test.txt', 'r')
file = open('input.txt', 'r')
score = 0
for a, b, c in zip(*[iter(file.readlines())]*3):
    res = [a.count(x) and b.count(x) and c.count(x) for x in string.ascii_letters]
    score = score + (res.index(sorted(res)[-1])+1)
print(score)
