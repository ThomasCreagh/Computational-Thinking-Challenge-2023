class GenerateNumbers():
    def __init__(self, working_set_amount, using_set_amount, file_name):
        self.WORKING_SET_AMOUNT = working_set_amount
        self.USING_SET_AMOUNT = using_set_amount
        self.FILE_NAME = file_name

        self.cached_numbers = {}
        self.fraction_list = []

    def write(self):
        wrote = False
        the_num = 0
        for lst in self.fraction_list:
            if round(1/lst[0], 14) != round(sum([1/i for i in lst[1]]), 14):
                print(lst[0], lst[1])
                quit()
        for lst in self.fraction_list:
            with open(self.FILE_NAME, "a") as writer:
                if lst[1] not in self.cached_numbers[lst[0]]:
                    if len(lst[1]) > ((self.USING_SET_AMOUNT
                                       + self.WORKING_SET_AMOUNT) - 1):
                        print(lst[0], lst[1])
                        quit()
                    the_num = lst[0]
                    number = lst[0]
                    number_list = lst[1]
                    writing_str = f"\n{number}:"
                    for num in range(len(number_list)):
                        if num == 0:
                            writing_str += f"{str(number_list[num])}"
                        else:
                            writing_str += f" {str(number_list[num])}"
                    writer.writelines(writing_str)
                    if lst[0] in self.cached_numbers:
                        self.cached_numbers[lst[0]].append(lst[1])
                    else:
                        self.cached_numbers[lst[0]] = [lst[1]]
                    wrote = True
        if wrote:
            print(f"wrote {the_num}")

    def set_growth(self):
        def filter_list(amount, lst):
            return list(filter(lambda x: len(x) == amount, lst))
        for number in range(200, 600):
            if number in self.cached_numbers:
                working_set = filter_list(
                    self.WORKING_SET_AMOUNT,
                    self.cached_numbers[number])
            else:
                continue

            for combination in working_set:
                for working_number in combination:
                    if working_number in self.cached_numbers:
                        using_set = filter_list(
                            self.USING_SET_AMOUNT,
                            self.cached_numbers[working_number])
                    else:
                        continue

                    set_without_working_number = combination[:]
                    set_without_working_number.remove(working_number)

                    for not_working_number in set_without_working_number:
                        using_set = list(filter(
                            lambda x: not_working_number not in x, using_set))

                    for additions in using_set:
                        list_output = [*set_without_working_number, *additions]
                        list_output.sort()
                        self.fraction_list.append((number, list_output))

            if self.fraction_list != []:
                self.write()

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

    def main(self):
        self.reader()
        print("Data loaded successfully.")
        print("adding_additions.py is starting...")
        self.set_growth()


seq = [(3, 3), (2, 4), (4, 2), (3, 4), (4, 3), (2, 5),
       (5, 2), (4, 4), (5, 3), (3, 5), (6, 2), (2, 6), (5, 4),
       (4, 5), (3, 6), (6, 3), (7, 2), (2, 7), (6, 6)]

for i in seq:
    print("Loading with seq: " + str(i))
    model_var = GenerateNumbers(i[0], i[1], "data.tom")
    model_var.main()
