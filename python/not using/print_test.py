from itertools import combinations

max_lst = [i for i in range(2, 2024)][742:]
print(max_lst, round(sum([1/i for i in max_lst])-1, 14), len(max_lst), 1/1000)

lst = [i for i in range(1000, 2024)]


for i in range(1, 1024):
    print(f"Amount: {i}")
    for combo in combinations(lst, i):
        if (round(sum([1/i for i in list(combo)]), 14) 
                == round(sum([1/i for i in max_lst])-1, 14)):
            print("oh?")
            print(combo)
            quit()
