
def sum_func(val, i):
    return 3+i if val == 0 else 6+i if (val == 1 or val == -2) else i


# file = open('test.txt', 'r')
file = open('input.txt', 'r')
fin = 0
for line in file.readlines():
    a, b = line.split()
    fin = fin + sum_func(ord(b) - ord(a) - 23, ord(b)-87)
print(fin)
