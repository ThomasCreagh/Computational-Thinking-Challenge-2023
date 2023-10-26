import json

with open("computed_numbers_testing.json", "r") as read_file:
    data = json.load(read_file)
    for i in range(2, 2023):
        lists = data[str(i)]
        if lists != []:
            for lst in lists:
                with open("data.tom", "a") as writer:
                    number = i
                    number_list = lst
                    writing_str = f"\n{number}:"
                    for num in range(len(number_list)):
                        if num != len(number_list)-1:
                            writing_str += f" {str(number_list[num])},"
                        else:
                            writing_str += f" {str(number_list[num])}"
                    writer.writelines(writing_str)
