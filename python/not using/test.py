import random
from datetime import datetime


class SplitNumbers():
    def __init__(self, lst, file_name):
        self.lst = set(lst)
        self.original = set(lst)
        self.FILE_NAME = file_name

        self.cached_numbers = {}
        self.fraction_list = []
        self.counter = 0
        self.index = 0
        self.done = True

    def reader(self):
        with open(self.FILE_NAME, "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = map(str.strip, line.split(':'))
                number_list = list(map(int, number_list.split(', ')))
                if number in self.cached_numbers:
                    self.cached_numbers[number].append(number_list)
                else:
                    self.cached_numbers[number] = [number_list]
                    self.cached_numbers = dict(sorted(self.cached_numbers.items()))

    def splitter(self):
        if self.index in self.cached_numbers:
            array = self.cached_numbers[self.index]
        else:
            return

        valid_list = [
            arrays for arrays in array if all(num not in self.lst for num in arrays)
        ]
        if valid_list:
            next_lists = [
            sum(len(self.cached_numbers[num]) for num in arrays)/len(arrays)
            for arrays in valid_list
            ]
            next_array = valid_list[next_lists.index(max(next_lists))]
            self.lst.remove(self.index)
            self.lst.update(next_array)
            self.lst = sorted(self.lst)
            if self.counter > 20:
                print(self.counter, len(self.lst), datetime.utcnow())
                self.counter = 0

    def reloop_self(self):
        while True:
            i = random.randint(2, 2023)
            if i in self.cached_numbers:
                combos = self.cached_numbers[i]
            else:
                continue

            combos_in_list = [
                combo for combo in combos if all(num in self.lst for num in combo)
            ]
            if combos_in_list:
                valid_combos = [combo for combo in combos if all(num not in self.lst for num in combo)]
            if valid_combos:
                in_list_combo_lens = [len(i) for i in combos_in_list]
                valid_combo_lens = [len(i) for i in valid_combos]
                min_list_combo = combos_in_list[in_list_combo_lens.index(min(in_list_combo_lens))]
                max_valid_combo = valid_combos[valid_combo_lens.index(max(valid_combo_lens))]

                if len(max_valid_combo) >= len(min_list_combo):
                    self.lst.difference_update(min_list_combo)
                    self.lst.update(max_valid_combo)
                    self.lst = sorted(self.lst)
                    self.done = False
                return

    def main(self):
        print("At:", datetime.utcnow())
        print(round(sum([1/i for i in self.lst]), 14), len(self.lst))
        self.reader()
        print("split_tom.py starting…")
        best_list = []
        while True:
            for self.index in self.lst:
                self.splitter()
            if self.done:
                if self.counter > 300:
                    if len(self.lst) > 800:
                        with open("lists.csv", "a") as writer:
                            writer.writelines(f"{str(len(self.lst))}, "
                                            f"{str(datetime.utcnow())}, "
                                            f"{str(self.lst)}\n")
                        if len(best_list) < len(self.lst):
                            best_list = self.lst

                            print("Most recent list:")
                            print(str(self.lst).replace(" ", ""),
                                round(sum([1/i for i in self.lst]), 14))
                            print("Recent list len", len(self.lst))
                            print()
                            print("Best list so far:")
                            print(str(best_list).replace(" ", ""),
                                round(sum([1/i for i in best_list]), 14))
                            print("Best list len", len(best_list))
                            print("At:", datetime.utcnow())
                            print("\nRestarting list…")
                            self.lst = self.original.copy()
                            self.counter = 0
                        else:
                            self.reloop_self()
                            self.done = True
                            self.counter += 1


if __name__ == '__main__':
    model_var = SplitNumbers([2, 3, 6], file_name="data.tom")
    model_var.main()
