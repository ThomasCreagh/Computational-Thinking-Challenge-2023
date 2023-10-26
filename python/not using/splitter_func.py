
def fraction_splitter(x):

    value1 = x+1
    value2 = x*(x+1)

    return value1, value2


lst = [2, 3, 6]
my_list = []

for item in lst:
    my_list.append(fraction_splitter(item))

print(my_list)


def fraction_splitter(x):
    value1 = x[0]+1
    value2 = x[0]*(x[0]+1)
    if value2 > 2023:
        x.append(x[0])
        return x
    else:
        x.append(fraction_splitter(value1))
        x.append(fraction_splitter(value2))
        return x


a, b = fraction_splitter(6)
print(a, b)

print(fraction_splitter([6]))
