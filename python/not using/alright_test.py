import random
from datetime import datetime


class SplitNumbers:
    def __init__(self, lst, file_name):
        self.lst = lst
        self.original = lst[:]
        self.FILE_NAME = file_name

        self.cached_numbers = {}
        self.fraction_list = []
        self.counter = 0
        self.index = 0
        self.done = True

    def valid_number(self, lst):
        return all(item not in self.lst for item in lst)

    def in_list(self, c):
        return all(number in self.lst for number in c)

    def not_in_list(self, c):
        return all(number not in self.lst for number in c)

    def read_file(self):
        with open(self.FILE_NAME, "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(", ")))

                if number in self.cached_numbers:
                    self.cached_numbers[number].append(number_list)
                else:
                    self.cached_numbers[number] = [number_list]
        self.cached_numbers = dict(sorted(self.cached_numbers.items()))

    def process_index(self):
        array = self.cached_numbers.get(self.index, [])
        if not len(array):
            return

        valid_list = [lst for lst in array if self.valid_number(lst)]
        if not len(valid_list):
            return

        next_lists = [
            sum(len(self.cached_numbers.get(number, []))
                for number in valid) / len(valid)
            for valid in valid_list
        ]

        max_next_list = valid_list[next_lists.index(max(next_lists))]
        self.lst.remove(self.index)
        self.lst.extend(max_next_list)
        self.lst.sort()

        # if len(self.lst) > 890:
        print(self.counter, round(
            sum([1 / i for i in self.lst])), len(self.lst), datetime.utcnow())
        self.counter = 0

    def reloop_self(self):
        while True:
            mm_score = []
            max_mins = []

            while len(mm_score) < 5:
                i = random.randint(2, 2023)
                combos = self.cached_numbers.get(i, [])
                if not combos:
                    continue

                combos_in_list = list(filter(self.in_list, combos))
                if not len(combos_in_list):
                    continue

                valid_combos = list(
                    filter(lambda c: self.not_in_list(c), combos))

                if not len(valid_combos):
                    continue

                min_list_combo = min(combos_in_list, key=len)
                max_valid_combo = max(valid_combos, key=len)
                if len(max_valid_combo) >= len(min_list_combo):
                    max_mins.append([min_list_combo, max_valid_combo])
                    mm_score.append(len(max_valid_combo) - len(min_list_combo))

            # if len(max_valid_combo) >= len(min_list_combo):
            if not len(mm_score):
                return

            best_min = max_mins[max(mm_score)][0]
            best_max = max_mins[max(mm_score)][1]
            pre_list = [number for number in self.lst[:]
                        if number not in best_min]
            pre_list.extend(best_max)
            pre_list.sort()
            self.lst = pre_list[:]
            self.done = False
            return

    def main(self):
        print("At:", datetime.utcnow())
        print(round(sum([1 / i for i in self.lst]), 14), len(self.lst))
        self.read_file()
        print("split_tom.py starting…")

        best_list = []

        while True:
            if len(best_list) < len(self.lst):
                best_list = self.lst[:]
                print(str(best_list).replace(" ", ""), round(
                    sum([1 / i for i in best_list]), 14))
                print("Best list len", len(best_list))
                if len(self.lst) > 899:
                    with open("lists2.csv", "a") as writer:
                        writer.writelines(
                            f"{str(len(self.lst))}, " f"{str(datetime.utcnow())}, " f"{str(self.lst)}\n")

            for self.index in self.lst:
                self.process_index()

            if self.done:
                self.reloop_self()
                self.done = True
                self.counter += 1


model_var = SplitNumbers([2, 3, 6], file_name="data.tom")

model_var.main()
