max_lst = [i for i in range(2, 2024)]

start_lst = max_lst[:757]
lst = max_lst[757:]

# print(start_lst)
# print(end_lst)

# print(sum([1/i for i in end_lst]))

# start_lst_sum = sum([1/i for i in start_lst])
# end_lst_sum = sum([1/i for i in end_lst])

# test_val = start_lst[697:698]
# i = 697
# while sum([1/i for i in test_val]) < 0.0017713968910760824:
#     i -= 1
#     test_val = start_lst[i:i+1]

# print(i)
# print(test_val)

# print(sum([1/i for i in test_val]))
# print(1-end_lst_sum)

# print(end_lst)


# # 1279

print(len(lst))

lowest_val = 1
index = 0
while True:
    lst_sum = sum([1/i for i in lst])

    if lst_sum == 1:
        break
    elif lst_sum < 1:
        # if (1 - lst_sum) < lowest_val:
        #     print(lowest_val)
        #     lowest_val = lst_sum
        lst[index] = lst[index] - 1
    elif lst_sum > 1:
        lst[index] = lst[index] + 1
        index += 1
    if index+1 == len(lst):
        index = 0
        lst[index] = lst[index] - 2

    # print(lst_sum)

print(lst)
