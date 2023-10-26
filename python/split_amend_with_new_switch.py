import random
from datetime import datetime


class SplitNumbers():
    def __init__(self, lst, file_name):
        self.lst = lst
        self.original = lst[:]
        self.FILE_NAME = file_name

        self.cached_numbers_split = {}
        self.cached_numbers_switch = {}
        self.fraction_list = []
        self.counter = 0
        self.index = 0
        self.done = True
        self.best_list = []

    def reader(self):
        with open(self.FILE_NAME[0], "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(" ")))

                if number in self.cached_numbers_split:
                    self.cached_numbers_split[number].append(number_list)
                else:
                    self.cached_numbers_split[number] = [number_list]
        self.cached_numbers_split = dict(sorted(self.cached_numbers_split.items()))

        with open(self.FILE_NAME[1], "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = round(float(number), 14)
                number_list = list(map(lambda c: round(float(c), 14), number_list.split(" ")))

                if number in self.cached_numbers_switch:
                    self.cached_numbers_switch[number].append(number_list)
                else:
                    self.cached_numbers_switch[number] = [number_list]
        self.cached_numbers_switch = dict(sorted(self.cached_numbers_switch.items()))

    def splitter(self):
        array = self.cached_numbers_split.get(self.index, [])
        if not len(array):
            return

        def is_valid(lst):
            return all(item not in self.lst for item in lst)

        valid_list = [lst for lst in array if is_valid(lst)]
        if not len(valid_list):
            return

        next_lists = [sum(len(self.cached_numbers_split.get(number, []))
                          for number in valid) / len(valid)
                      for valid in valid_list]

        max_next_list = valid_list[next_lists.index(max(next_lists))]
        self.lst.remove(self.index)
        self.lst.extend(max_next_list)
        self.lst.sort()

        print(self.counter, round(sum([1/i for i in self.lst])),
              len(self.lst), datetime.utcnow())
        self.counter = 0

    def reloop_self(self):
        while True:
            mm_score = []
            max_mins = []
            while len(mm_score) < 2:
                key_lst = list(self.cached_numbers_switch.keys())
                i = key_lst[random.randint(0, len(key_lst)-1)]
                combos = self.cached_numbers_switch.get(i, [])
                if not combos:
                    continue

                def in_list(c):
                    return all(number in self.lst for number in c)

                def not_in_list(c):
                    return all(number not in self.lst for number in c)
                combos_in_list = list(filter(in_list, combos))
                if not len(combos_in_list):
                    continue

                valid_combos = list(filter(lambda c: not_in_list(c), combos))

                if not len(valid_combos):
                    continue

                min_list_combo = min(combos_in_list, key=len)
                max_valid_combo = max(valid_combos, key=len)

                max_mins.append([min_list_combo, max_valid_combo])
                mm_score.append(len(max_valid_combo) - len(min_list_combo))

            # if len(max_valid_combo) >= len(min_list_combo):
            if not len(mm_score):
                return
            if max_mins:
                best_min = max_mins[mm_score.index(max(mm_score))][0]
                best_max = max_mins[mm_score.index(max(mm_score))][1]
                pre_list = [number for number in self.lst[:]
                            if number not in best_min]
                pre_list.extend(best_max)
                pre_list.sort()
                self.lst = pre_list[:]
                self.done = False
            return

    def best_list_check(self):
        if len(self.best_list) < len(self.lst):
            self.best_list = self.lst[:]
            if len(self.lst) > 900:
                with open("lists.csv", "a") as writer:
                    writer.writelines(f"{str(len(self.lst))}, "
                                      f"{str(datetime.utcnow())}, "
                                      f"{str(self.lst)}\n")

        print(str(self.lst).replace(" ", ""),
              round(sum([1/i for i in self.lst]), 14))
        print("Recent list len", len(self.lst))

        print(str(self.best_list).replace(" ", ""),
              round(sum([1/i for i in self.best_list]), 14))
        print("Best list len", len(self.best_list))

    def main(self):
        print("At:", datetime.utcnow())
        print(round(sum([1/i for i in self.lst]), 14), len(self.lst))
        self.reader()
        print("split_tom.py starting…")

        while True:
            self.best_list_check()
            for self.index in self.lst:
                self.splitter()
            self.best_list_check()
            self.reloop_self()
            # if self.done:
            #     self.reloop_self()
            #     self.done = True
            #     self.counter += 1


model_var = SplitNumbers([22,27,29,31,32,33,34,35,36,37,38,40,42,44,46,48,49,54,55,56,60,63,64,66,70,75,76,80,84,88,90,96,98,99,105,108,120,126,128,160,165,168,175,180,184,189,192,198,210,220,225,231,234,240,243,256,272,273,280,288,294,297,300,324,330,336,350,368,375,378,384,396,420,432,450,459,468,480,486,500,504,512,513,540,544,546,560,570,576,588,594,600,640,648,660,672,675,693,700,702,720,736,756,759,768,810,812,825,828,840,864,875,880,918,924,930,945,960,972,975,990,1000,1026,1050,1056,1080,1100,1120,1122,1140,1152,1190,1260,1296,1320,1332,1344,1386,1400,1440,1500,1512,1518,1536,1650,1656,1680,1800,1806,1890,1892,1900,1920,1944,1950,1980,2000,2016],
                         file_name=("data_new.tom", "data_switch_1.tom"))

model_var.main()
