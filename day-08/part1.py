def visible(h,arr):
    return len(list(filter(lambda x: x < h, arr))) == len(arr)

#file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
file = open('input.txt', 'r', encoding='utf-8').read().splitlines()

arr2d = []
for i in file:
    arr2d.append(list(map(int,list(i))))

arr_len = len(arr2d)
visible_tree_count = arr_len * 4 - 4
for i in range(1, arr_len - 1):
    for j in range(1, arr_len - 1):
        col = [row[j] for row in arr2d]
        a = visible(arr2d[i][j], arr2d[i][0:j])
        b = visible(arr2d[i][j], arr2d[i][j+1:arr_len])
        c = visible(arr2d[i][j], col[0:i])
        d = visible(arr2d[i][j], col[i+1:arr_len])
        visible_tree_count = visible_tree_count + (1 if a or b or c or d else 0)

print(visible_tree_count)
