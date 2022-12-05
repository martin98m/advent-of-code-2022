file = open('test.txt', 'r')
# file = open('input.txt', 'r')
p1_count, p2_count = 0, 0
for line in file.readlines():
    x = [x.split('-') for x in line.split(',')]
    arr1 = range(int(x[0][0]),int(x[0][1])+1)
    arr2 = range(int(x[1][0]),int(x[1][1])+1)
    res1 = [x in arr1 for x in arr2]
    res2 = [x in arr2 for x in arr1]
    if res1.count(True) == len(res1) or res2.count(True) == len(res2):
        p1_count = p1_count + 1
    if res1.count(True) > 0:
        p2_count = p2_count + 1
print(p1_count)
print(p2_count)
