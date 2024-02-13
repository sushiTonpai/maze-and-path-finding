import random

adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(random.choice(adj))

ROWS = 2
COLS = 3
array_2d = [[i for i in range(0, COLS)] for j in range(0, ROWS)]
print(array_2d)
print(array_2d[0][1])

tile = [(2,2), (4,4)]
path = [(1,2), (3,4)]
my_dic = {}
my_dic.update({tile:path})
print(my_dic)

