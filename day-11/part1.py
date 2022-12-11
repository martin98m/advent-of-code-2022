class Monke():
   
    count = 0

    def __init__(self, item_Arr, new_multi, test, throw) -> None:
        self.items = item_Arr
        self.multi = new_multi
        self.test = test
        self.throw = throw

    def catch_banana(self, item):
        self.items.append(item)

    def throw_bananas(self):
        self.count = self.count + len(self.items)
        for old in self.items:
            q = eval(self.multi) // 3
            test = q % self.test == 0
            monke_arr[self.throw[test]].catch_banana(q)
        self.items = []

#file = open('test.txt', 'r', encoding='utf-8').read().split('\n\n')
file = open('input.txt', 'r', encoding='utf-8').read().split('\n\n')

monke_arr = []

for monke in file:
    monke = monke.splitlines()
    items = [int(x) for x in monke[1].split(':')[1].split(',')]
    new_multi = monke[2].split('=')[1]
    test = int(monke[3].split('by')[1])
    throw = {True: int(monke[4].split('monkey')[1]), False: int(monke[5].split('monkey')[1])}
    monke_arr.append(Monke(items, new_multi, test, throw))

for check_round in range(20):
    for monke in monke_arr:
        monke.throw_bananas()

qqq = [monke.count for monke in monke_arr]
print(sorted(qqq)[-1] * sorted(qqq)[-2])
