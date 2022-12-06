#file = open('test.txt', 'r')
inp = open('input.txt', 'r').read()
size = 4
for i in range(len(inp)-size-1):
    if len(set(inp[i:i+size])) == size:
        print(i+size)
        break