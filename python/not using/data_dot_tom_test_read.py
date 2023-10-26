with open("data.tom", "r") as reader:
    cached_nums = []
    data = reader.readlines()
    for line in data:
        number = int(str(line.split(":")[0]))
        number_list = str(line).split(":")[1].split(", ")
        number_list[-1] = number_list[-1].replace("\n", "")
        number_list = list(map(int, number_list))
        cached_nums.append((number, number_list))
    print(cached_nums)
