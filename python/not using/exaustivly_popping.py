from tqdm import tqdm
from itertools import combinations

max_lst = [i for i in range(2, 31)]

lst = max_lst


for i in tqdm(range(15, 2022)):
    for combo in combinations(lst, i):
        print(combo)
        test_lst = lst[:]
        for j in combo:
            test_lst.remove(j)
        lst_sum = sum([1/i for i in test_lst])
        if lst_sum == 1:
            print()
            print(test_lst)
            print(lst_sum)
            quit()
        # print(test_lst)
