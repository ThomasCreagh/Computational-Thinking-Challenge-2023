from itertools import combinations
import json
import math
import concurrent.futures


class Model():
    def __init__(self, lst, generate, fraction_amount, file_name):
        self.lst = lst
        self.original = lst[:]
        self.GENERATE = generate
        self.FRACTION_AMOUNT = fraction_amount
        self.FILE_NAME = file_name

        self.fraction_list = []
        self.index = 0
        self.done = True
        self.combo_sum_dict = {}  # dictionary to store the sum of fractions for each combination
        self.processed_combos = set()  # set to store combinations that have already been processed

    def write(self, num, combo_list):
        with open(self.FILE_NAME, "r") as read_file:
            data = json.load(read_file)
            for combo in combo_list:
                if combo not in data[str(num)]:
                    data[str(num)] += [combo]
            with open(self.FILE_NAME, "w") as write_file:
                json.dump(data, write_file)

    def get_combo_sum(self, combo):
        # check if the sum of fractions for the given combination is already in the dictionary
        if combo in self.combo_sum_dict:
            return self.combo_sum_dict[combo]

        # compute the sum of fractions for the given combination
        combo_sum = sum(1/i for i in combo)

        # store the computed value in the dictionary
        self.combo_sum_dict[combo] = combo_sum

        return combo_sum

    def check_fraction_sum(self, combo, num):
        combo_sum = self.get_combo_sum(combo)  # use the stored value or compute it if necessary
        gcd = math.gcd(1, int(combo_sum * 10**14))
        return int(combo_sum * 10**14) // gcd == int((1/num) * 10**14)

    def process_combo(self, combo):
        if combo in self.processed_combos:
            return

        for i in range(125, min(combo)):
            if self.check_fraction_sum(combo, i):
                self.write(i, [combo])
                print(f"new {i} combo: {combo}")
                self.processed_combos.add(combo)

    def combos(self):
        self.fraction_list = []
        last_combo = 0
        min_fraction = 393
        max_fraction = 2024
        combos = (combo for combo in combinations(range(393, 2024), self.FRACTION_AMOUNT)
                  if min_fraction in combo and max_fraction <= sum(combo) - max_fraction)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for combo in combos:
                if combo[0] != last_combo:
                    print(combo[0])
                executor.submit(self.process_combo, combo)
                last_combo = combo[0]

    def main(self):
        print(self.lst, round(sum([1/i for i in self.lst]), 14), len(self.lst))
        while True:
            print("Loop")
            self.combos()


model_var = Model([2, 3, 6],
                  generate=True,
                  fraction_amount=3,
                  file_name="computed_numbers.json")
model_var.main()
