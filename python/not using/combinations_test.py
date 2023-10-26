from itertools import combinations

lst = [i for i in range(2, 2024)]

for combo in combinations(lst, 2):
    print(combo)
