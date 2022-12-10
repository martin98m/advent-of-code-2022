move = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
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
    (-1,-2):(-1,-1),

    (2,2):(1,1),
    (-2,2):(-1,1),
    (2,-2):(1,-1),
    (-2,-2):(-1,-1),
    }


def idk(h, t):
    xxx = tuple(map(lambda q, e: q - e, h, t))
    return tuple(map(lambda q, e: q + e, t, move2[xxx])) if xxx in move2 else t

#file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
file = open('input.txt', 'r', encoding='utf-8').read().splitlines()

aaaaaa = []
bbbbbb = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
for i in file:
    cmd, val = i.split()
    for x in range(int(val)):
        #print(bbbbbb)
        bbbbbb[0] = tuple(map(lambda q, e: q + e, bbbbbb[0], move[cmd]))
        
        for x in range(1,10):
            fml = idk(bbbbbb[x-1],bbbbbb[x])
            if x == 9:
                
                aaaaaa.append(fml)
            bbbbbb[x] = fml
        


print(len(set(aaaaaa)))
