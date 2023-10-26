from itertools import combinations
import json

lst = [2]

GEN_LST = [i for i in range(470, 2024)]
GENERATE = True
FRACTION_AMOUNT = 2

# TODO: make compatible for all numbers

print(lst, round(sum([1/i for i in lst]), 14), len(lst))


def write_data(x, fraction_list):
    if fraction_list != []:
        with open("computed_numbers.json", "r") as read_file:
            data = json.load(read_file)
            fraction_list.append([0, 0])
            for item in fraction_list:
                print(item, data[str(x)])
                if item not in data[str(x)]:
                    data[str(x)] += [item]
            with open("computed_numbers.json", "w") as write_file:
                json.dump(data, write_file)


def combos(x, FRACTION_AMOUNT):
    fraction_list = []
    for combo in combinations(range(x, 2024), FRACTION_AMOUNT):
        if (round(sum([1/i for i in list(combo)]), 14)
                == round(1/x, 14)):
            fraction_list.append(list(combo))
            print(fraction_list)
    return fraction_list


def main(lst, GEN_LST, GENERATE, FRACTION_AMOUNT):
    while True:
        done = True
        if not GENERATE:
            for x in lst:
                with open("computed_numbers.json", "r") as read_file:
                    data = json.load(read_file)
                    items = data[str(x)]
                    if items != []:
                        for i in items:
                            valid = True
                            for j in i:
                                if j in lst:
                                    valid = False
                            if valid:
                                lst.remove(x)
                                for j in i:
                                    lst.append(j)
                                lst.sort()
                                print()
                                print(lst, round(
                                    sum([1/i for i in lst]), 14), len(lst))
                                done = False
                                break

        else:
            for x in GEN_LST:
                done = False
                fraction_list = combos(x, FRACTION_AMOUNT)
                write_data(x, fraction_list)
        if done:
            break


main(lst, GEN_LST, GENERATE, FRACTION_AMOUNT)
