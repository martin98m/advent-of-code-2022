def scenic(h, arr):
    res = [n for n,i in enumerate(arr) if i >= h]
    return len(arr) if len(res) == 0 else res[0] + 1

#file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
file = open('input.txt', 'r', encoding='utf-8').read().splitlines()

aaaaaa, arr2d = [], []
for i in file:
    arr2d.append(list(map(int,list(i))))

arr_len = len(arr2d)
for i in range(1, arr_len-1):
    for j in range(1, arr_len-1):
        col = [row[j] for row in arr2d]
        a = scenic(arr2d[i][j], arr2d[i][0:j][::-1])
        b = scenic(arr2d[i][j], arr2d[i][j+1:arr_len])
        c = scenic(arr2d[i][j], col[0:i][::-1])
        d = scenic(arr2d[i][j], col[i+1:arr_len])
        aaaaaa.append(a*b*c*d)

print(sorted(aaaaaa)[-1])
