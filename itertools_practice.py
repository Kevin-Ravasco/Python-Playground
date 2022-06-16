from itertools import product

a = [1, 2, 3]
b = [4, 5, 6]

objects = list(product(a, b))

for i in objects:
    print(i)
