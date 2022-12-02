
dic = {
    'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7
}

# file = open('test.txt', 'r')
file = open('input.txt', 'r')
score = 0
for line in file.readlines():
    score = score + dic[line.replace('\n', '')]
print(score)
