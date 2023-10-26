import random
from datetime import datetime


class SplitNumbers():
    def __init__(self, lst, file_name):
        self.lst = lst
        self.origanal = lst[:]
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
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(" ")))

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

        valid_list = []
        if array != []:
            for lists in array:
                valid = True
                for items in lists:
                    if items in self.lst:
                        valid = False
                if valid:
                    valid_list.append(lists)
            if valid_list != []:
                next_lists = []
                for valid in valid_list:
                    temp = []
                    for number in valid:
                        if number in self.cached_numbers:
                            number_array = self.cached_numbers[number]
                        else:
                            continue

                        temp.append(len(number_array))
                    if temp != []:
                        next_lists.append(sum(temp)/len(temp))
                    else:
                        next_lists.append(0)

                self.lst.remove(self.index)
                for items_append in valid_list[
                        next_lists.index(max(next_lists))]:
                    self.lst.append(items_append)
                self.lst.sort()
                # print(self.counter, len(self.lst), datetime.utcnow())

    def reloop_self(self):
        while True:
            i = random.randint(2, 2023)
            if i in self.cached_numbers:
                combos = self.cached_numbers[i]
            else:
                continue

            combos_in_list = []
            for combo in combos:
                in_list = True
                for number in combo:
                    if number not in self.lst:
                        in_list = False
                if in_list:
                    combos_in_list.append(combo)
            if combos_in_list != []:
                valid_combos = []
                for combo in combos:
                    valid = True
                    for number in combo:
                        if number in self.lst:
                            valid = False
                    if valid:
                        valid_combos.append(combo)

                    if valid_combos != []:
                        in_list_combo_lens = [len(i) for i in combos_in_list]
                        valid_combo_lens = [len(i) for i in valid_combos]

                        min_list_combo = combos_in_list[
                            in_list_combo_lens.index(min(in_list_combo_lens))]
                        max_valid_combo = valid_combos[
                            valid_combo_lens.index(max(valid_combo_lens))]

                        if len(max_valid_combo) >= len(min_list_combo):
                            for number in min_list_combo:
                                self.lst.remove(number)
                                # print(f"removed {number}")
                            for number in max_valid_combo:
                                # print(f"added {number}")
                                self.lst.append(number)
                            self.lst.sort()
                            self.done = False
                            return

    def main(self):
        print("At:", datetime.utcnow())
        print(round(sum([1/i for i in self.lst]), 14), len(self.lst))
        self.reader()
        print("split_tom.py starting...")
        best_list = []
        while True:
            print(round(sum([1/i for i in self.lst]), 14), len(self.lst))
            for self.index in self.lst:
                self.splitter()
            if self.done:
<<<<<<< HEAD:school/projects/1000_for_ms/python/split_tom.py
                if self.counter > 200:
=======
                if self.counter > 100:
                    if len(self.lst) > 800:
                        with open("lists.csv", "a") as writer:
                            writer.writelines(f"{str(len(self.lst))}, "
                                              f"{str(datetime.utcnow())}, "
                                              f"{str(self.lst)}\n")
>>>>>>> c377ca60ef1e10651ac94735da52c707113b0c48:school/projects/1000_for_ms/python/not using/split_tom.py
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

                    print("\nRestarting list...")
                    self.lst = self.origanal[:]
                    self.counter = 0
                else:
                    self.reloop_self()
                    self.done = True
                self.counter += 1
                # omg


model_var = SplitNumbers([2, 3, 6],
                         file_name="data_test.tom")

model_var.main()
