import random

adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(random.choice(adj))

ROWS = 2
COLS = 3
array_2d = [[i for i in range(0, COLS)] for j in range(0, ROWS)]
print(array_2d)
print(array_2d[0][1])
