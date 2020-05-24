from random import randint
import random

max = 10000
value_field = []
for i in range(20):
    value_field.append(max)
for i in range(20, 101):
    value_field.append(i)
    
size = 10
map = []
for i in range(size):
    map.append([0]*size)
    
for i in range(size):
    for j in range(i, size):
        if i == j:
            map[i][j] = max
            map[j][i] = map[i][j]
        else:
            # r = randint(0, 2)
            # if r == 0:
            #     map[i][j] = "max"
            #     map[j][i] = map[i][j]
            # if r == 1:
            #     map[i][j] = randint(1, 50)
            #     map[j][i] = map[i][j]
            # if r == 2:
            #     map[i][j] = randint(50, 100)
            #     map[j][i] = map[i][j]
            map[i][j] = random.choice(value_field)
            map[j][i] = map[i][j]
                
for i in map:
    print(i)
    
with open('map.txt', 'w', encoding='utf-8') as w:
    w.write(str(size) + '\n')
    for i in map:
        for j in i:
            w.write(str(j) + " ")
        w.write('\n')
    w.close()
