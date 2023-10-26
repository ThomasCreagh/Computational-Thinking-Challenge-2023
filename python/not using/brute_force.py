# to slow
from itertools import combinations
import csv

start = 2
end = 758

lst = [i for i in range(start, end)]

for combo_length in range(3, 2024):
    new_combo = False
    last_combo = 1
    for combo in combinations(lst, combo_length):
        if combo[0] != last_combo:
            print(f"{((combo[0]-1)/end)*100}% "
                  f"of combo length: {combo_length}")

        if (sum([1/i for i in combo]) == 0.30586456865590017):
            with open("combos.csv", "a", newline="\n") as _file:
                data_writer = csv.writer(_file)
                data_writer.writerow((combo_length, combo, end))
            print(f"new combo: {combo}")
            new_combo = True
            start = combo[0]
            break

        last_combo = combo[0]
