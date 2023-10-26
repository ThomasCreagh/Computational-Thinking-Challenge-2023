def factors(x):
    return [i/x for i in range(1, x+1) if x % i == 0]


fac_lst = factors(20000)
# print([sum(list(reversed(fac_lst))[i:]) for i in range(len(fac_lst))])
print(fac_lst)
print([round(i, 15).as_integer_ratio() for i in fac_lst])
