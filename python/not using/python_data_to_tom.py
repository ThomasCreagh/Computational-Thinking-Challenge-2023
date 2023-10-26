with open("text_test.tom", "a") as writer:
    number = 2
    number_list = [3, 4, 5, 6]
    writing_str = f"\n{number}:"
    for num in range(len(number_list)):
        if num != len(number_list)-1:
            writing_str += f" {str(number_list[num])},"
        else:
            writing_str += f" {str(number_list[num])}"
    writer.writelines(writing_str)


with open("text_test.tom", "r") as reader:
    data = reader.readlines()
    integer = 2
    for line in data:
        if f"{integer}:" in line:
            number = int(str(line.split(":")[0]))
            number_list = str(line).split(":")[1].split(", ")
            number_list[-1] = number_list[-1].replace("\n", "")
            number_list = list(map(int, number_list))
            print(number, number_list)
