from itertools import combinations

lst = [2, 3, 6]
while True:
    best_lst = []
    best_sum = []
    # remove 1 replace with 2
    for i in range(2, len(lst)+1):
        test_lst = lst[:]
        test_lst.pop(-i)
        if i == len(lst):
            lst_1 = [i for i in range(lst[-i], lst[-i+1])]
        else:
            lst_1 = [i for i in range(lst[-i-1]+1, lst[-i+1])]

        lst_2 = [i for i in range(lst[-1]+1, (lst[-1]*2)+1)]
        combo_lst = lst_1 + lst_2
        for combo in combinations(combo_lst, 2):
            test_lst_2 = test_lst[:]
            test_lst_2.append(combo[0])
            test_lst_2.append(combo[1])
            test_lst_2.sort()
            if sum([1/i for i in test_lst_2]) == 1:
                best_lst.append(test_lst_2[:])
                best_sum.append(test_lst_2[-1])

    # # remove 2 replace with 3
    # for i in combinations(range(len(lst)), 2):
    #     test_lst = lst[:]
    #     test_lst.pop(i[0])
    #     test_lst.pop(i[1])
    #     if i == len(lst):
    #         lst_1 = [i for i in range(lst[-i], lst[-i+1])]
    #     else:
    #         lst_1 = [i for i in range(lst[-i-1]+1, lst[-i+1])]

    #     lst_2 = [i for i in range(lst[-1], (lst[-1]*2)+1)]
    #     lst_3 = [i for i in range(lst[-1], (lst[-1]*2)+1)]

    #     combo_lst = lst_1 + lst_2 + lst_3
    #     for combo in combinations(combo_lst, 2):
    #         test_lst_2 = test_lst[:]
    #         test_lst_2.append(combo[0])
    #         test_lst_2.append(combo[1])
    #         test_lst_2.sort()
    #         if sum([1/i for i in test_lst_2]) == 1:
    #             print(test_lst_2)
    #             print(sum([1/i for i in test_lst_2]))

    lst = best_lst[best_sum.index(min(best_sum))]
    print(lst)
    print(sum([1/i for i in lst]))
    print(len(lst))
