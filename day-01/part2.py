# file = open('test.txt', 'r')
file = open('input.txt', 'r')
i, arr = 0, [0]*1000
for line in file.readlines():
    if len(line[:-1]) != 0:
        arr[i] = arr[i] + int(line)
    else:
        i = i + 1
print(sum(sorted(arr, reverse=True)[:3]))
# print(sorted(arr, reverse=True)[0])
