class GenerateNumbers():
    def __init__(self, file_name_in, file_name_out):
        self.FILE_NAME_IN = file_name_in
        self.FILE_NAME_OUT = file_name_out
        self.cached_numbers = {}
        self.numbers_to_choose_from = []

    def write(self):
        for i in self.numbers_to_choose_from:
            lst = self.cached_numbers[i]
            for j in lst:
                with open(self.FILE_NAME_OUT, "a") as writer:
                    number = i
                    number_list = j
                    writing_str = f"\n{number}:"
                    for num in range(len(number_list)):
                        if num != len(number_list)-1:
                            writing_str += f" {str(number_list[num])},"
                        else:
                            writing_str += f" {str(number_list[num])}"
                    writer.writelines(writing_str)

    def reader(self):
        with open(self.FILE_NAME_IN, "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(" ")))

                if number in self.cached_numbers:
                    self.cached_numbers[number].append(number_list)
                else:
                    self.numbers_to_choose_from.append(number)
                    self.cached_numbers[number] = [number_list]

        self.cached_numbers = dict(sorted(
            self.cached_numbers.items()))

    def main(self):
        self.reader()
        self.write()


model_var = GenerateNumbers("data_new.tom", "data_sorted.tom")
model_var.main()
