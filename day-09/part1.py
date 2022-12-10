move = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1), 'UL':(-1,1), 'UR':(1,1), 'DL':(-1,-1), 'DR':{1,-1}}
move2 = {
    (2,0):(1,0), 
    (-2,0):(-1,0), 
    (0,2):(0,1), 
    (0,-2):(0,-1), 
    
    (2,1):(1,1), 
    (-2,1):(-1,1), 
    (2,-1):(1,-1), 
    (-2,-1):(-1,-1),

    (1,2):(1,1), 
    (-1,2):(-1,1), 
    (1,-2):(1,-1), 
    (-1,-2):(-1,-1)
    }


def idk(h, t):
    xxx = tuple(map(lambda q, e: q - e, h, t))
    return tuple(map(lambda q, e: q + e, t, move2[xxx])) if xxx in move2 else t

#file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
file = open('input.txt', 'r', encoding='utf-8').read().splitlines()

aaaaaa = []
head, tail = (0,0), (0,0)
for i in file:
    cmd, val = i.split()
    for x in range(int(val)):
        head = tuple(map(lambda q, e: q + e, head, move[cmd]))
        tail = idk(head, tail)
        aaaaaa.append(tail)

print(len(set(aaaaaa)))
