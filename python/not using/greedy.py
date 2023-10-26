import math

MIN_X = 2
MAX_X = 2023

fractions = []
remaining_sum = 1

for i in range(2, 1218):
    for x in range(MAX_X, MIN_X - 1, -1):
        if len(fractions) == i:
            break
        frac = 1 / x
        if frac <= remaining_sum:
            fractions.append(frac)
            remaining_sum -= frac

    if math.isclose(remaining_sum, 0):
        print(fractions)
    else:
        print(f"No set of {i}  rationals in the form 1/x that sum to 1 exists.")