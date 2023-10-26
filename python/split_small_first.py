from random import randint, shuffle
from datetime import datetime
# import time


class FractionSumFinder:
    def __init__(self, number_list, file_name):
        self.number_set = set(number_list)
        self.FILE_NAME = file_name

        self.cached_combinations = {}
        self.reverse_lookup = {}
        self.numbers_to_choose_from = []
        self.best_set = {}
        self.best_combination = False
        self.can_remove = {}

    def read_data(self):
        with open(self.FILE_NAME, "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(" ")))

                if number in self.cached_combinations:
                    self.cached_combinations[number].append(number_list)
                else:
                    self.numbers_to_choose_from.append(number)
                    self.cached_combinations[number] = [number_list]

                for number_list_number in number_list:
                    if number_list_number in self.reverse_lookup:
                        if number in self.reverse_lookup[number_list_number]:
                            continue
                        self.reverse_lookup[number_list_number].append(number)
                    else:
                        self.reverse_lookup[number_list_number] = [number]

        self.cached_combinations = dict(sorted(
            self.cached_combinations.items()))

    def random_extreme(self, lst, func):
        lst = list(filter(lambda x: len(x) == len(func(lst, key=len)), lst))
        return lst[randint(0, len(lst)-1)]

    # def removing_numbers_check(self):
    #     for get_rid_of_number in self.number_set:
    #         get_rid_of_parents = self.reverse_lookup[get_rid_of_number]
    #         for children in get_rid_of_parents:
    #             split_combinations = self.cached_combinations.get(
    #                 children, set())

    #             valid_add_combinations = list(
    #                 filter(lambda c: get_rid_of_number not in c and all(
    #                     i not in self.number_set for i in c),
    #                        split_combinations))

    #             valid_remove_combinations = list(
    #                 filter(lambda c: get_rid_of_number in c and all(
    #                     i in self.number_set for i in c),
    #                        split_combinations))

    #             if (not len(valid_add_combinations)
    #                     or not len(valid_remove_combinations)):
    #                 continue

    #             if (len(max(valid_add_combinations, key=len))
    #                     >= len(min(valid_remove_combinations, key=len))):
    #                 number_list = [max(valid_add_combinations, key=len),
    #                                min(valid_remove_combinations, key=len)]

    #                 if get_rid_of_number in self.can_remove:
    #                     self.can_remove[
    #                         get_rid_of_number].append(number_list)
    #                 else:
    #                     self.can_remove[get_rid_of_number] = [number_list]

    # def replace_smartly(self):
    #     replacables = []
    #     for set_item in self.number_set.intersection(
    #             set(self.numbers_to_choose_from)):
    #         split_combinations = self.cached_combinations.get(
    #             set_item, set())

    #         can_remove_numbers = self.can_remove.keys()

    #         for i in split_combinations:
    #             valid = True
    #             number_in_list = False
    #             for j in i:
    #                 if j in self.number_set:
    #                     if number_in_list:
    #                         valid = False
    #                     number_in_list = True
    #                     if j not in can_remove_numbers:
    #                         valid = False

    #             if valid and number_in_list:
    #                 replacables.append((set_item, i))

    #     print("\ncan remove:", self.can_remove)
    #     print("\nreplacables:", replacables)
    #     if len(replacables):
    #         working_list = []
    #         for replacing in replacables:
    #             for i in replacing[1]:
    #                 if i in self.number_set:

    #                     add_to_set = self.can_remove[i][0][0]
    #                     remove_from_set = self.can_remove[i][0][1]

    #                     if (replacing[0] in add_to_set
    #                             or replacing[0] in remove_from_set):
    #                         break

    #                     if len(set(add_to_set).intersection(
    #                             set(replacing[1]))) > 0:
    #                         break

    #                     if len(set(remove_from_set).intersection(
    #                             set(replacing[1]))) > 1:
    #                         break

    #                     working_list.append(replacing)
    #         print("\nworking_list", working_list)
    #         if len(working_list):
    #             replacing = working_list[randint(0, len(working_list)-1)]
    #             for i in replacing[1]:
    #                 if i in self.number_set:

    #                     add_to_set = self.can_remove[i][0][0]
    #                     remove_from_set = self.can_remove[i][0][1]

    #                     print("\nremove:", remove_from_set)
    #                     print("add:", add_to_set)
    #                     print()

    #                     self.number_set = self.number_set.difference(
    #                         set(remove_from_set)).union(
    #                         set(add_to_set))

    #             print("remove for 1:", replacing[0])
    #             print("add for 1:", replacing[1])
    #             self.number_set = self.number_set.difference(
    #                 {replacing[0]}).union(
    #                 set(replacing[1]))
    def validate_combinations(self, add, remove, formated_list):
        print(add, remove, formated_list)

    def check_combo(self, input_list):
        def one_in_list(c):
            k = 0
            for i in c:
                if i not in self.number_set:
                    k += 1
            if k < len(c)-1:
                return False

            return True

        hit_switchable = False
        for verifying_group in input_list:
            rid_of_number = verifying_group[0]
            get_rid_of_parents = self.reverse_lookup[rid_of_number]
            for parent in get_rid_of_parents:
                split_combinations = self.cached_combinations.get(
                    parent, set())

                add = list(
                    filter(lambda c: rid_of_number not in c and all(
                        i not in self.number_set for i in c),
                        split_combinations))

                remove = list(
                    filter(lambda c: rid_of_number in c and all(
                        i in self.number_set for i in c),
                            split_combinations))

                if len(add) != 0 and len(remove) != 0:
                    hit_switchable = True
                    self.validate_combinations(add, remove, input_list)

            if not hit_switchable:
                for parent in get_rid_of_parents:
                    split_combinations = self.cached_combinations.get(
                        parent, set())

                    remove = list(
                        filter(lambda c: rid_of_number in c and all(
                            i in self.number_set for i in c),
                                split_combinations))

                    add_one_in = list(
                        filter(lambda c: rid_of_number not in c
                               and one_in_list(c),
                               split_combinations))

                    # removing instead of adding. one in, instead of one out

                    if len(remove) != 0 and len(add_one_in) != 0:
                        formatted_list = []
                        for pair in add_one_in:
                            for item in pair:
                                if item in self.number_set:
                                    pair.remove(item)
                                    formatted_list.append((item, pair))
                                    break

                        print(self.check_combo(formatted_list))

        # for rid_of_pair in number_combos:
        #     valid_check = []
        #     for rid_of_number in rid_of_pair:
        #         get_rid_of_parents = self.reverse_lookup[rid_of_number]
        #         for parent in get_rid_of_parents:
        #             split_combinations = self.cached_combinations.get(
        #                 parent, set())

        #             def one_in_list(c):
        #                 k = 0
        #                 for i in c:
        #                     if i not in self.number_set:
        #                         k += 1
        #                 if k < len(c)-1:
        #                     return False

        #                 return True

        #             add = list(
        #                 filter(lambda c: rid_of_number not in c and all(
        #                     i not in self.number_set for i in c),
        #                     split_combinations))

        #             add_one_in = list(
        #                 filter(lambda c: rid_of_number not in c
        #                        and one_in_list(c),
        #                        split_combinations))

        #             remove = list(
        #                 filter(lambda c: rid_of_number in c and all(
        #                     i in self.number_set for i in c),
        #                         split_combinations))

        #             print(rid_of_number, parent, "add", add)
        #             print(rid_of_number, parent, "remove", remove)
        #             valid_check.append((rid_of_number, parent, add, add_one_in, remove))
        #         self.validate_combinations(valid_check)
        #     print("k")

    def depth(self, number):
        number_combos = self.cached_combinations.get(number, [])

        def one_in_list(c):
            k = 0
            for i in c:
                if i not in self.number_set:
                    k += 1
            if k < len(c)-1:
                return False
            return True

        list_one_in = list(
            filter(lambda c: one_in_list(c),
                   number_combos))

        formatted_list = []
        for pair in list_one_in:
            for item in pair:
                if item in self.number_set:
                    pair.remove(item)
                    formatted_list.append((item, pair))
                    break

        # look_for = set([i for j in number_combos for i in j])
        self.check_combo(formatted_list)

    def removing_numbers_check(self):
        smallest_number = list(self.number_set)[0]
        self.depth(smallest_number)
        # smallest_number_combos = self.cached_combinations.get(smallest_number, [])
        # look_for = set([i for j in smallest_number_combos for i in j])
        # for item in look_for:

        # get_rid_of_parents = self.reverse_lookup[get_rid_of_number]
        # for parent in get_rid_of_parents:
        #     split_combinations = self.cached_combinations.get(
        #         parent, set())

        #     def one_in_list(c):
        #         k = 0
        #         for i in c:
        #             if i not in self.number_set:
        #                 k += 1
        #         if k < len(c)-1:
        #             return False

        #         return True

        #     v = list(
        #         filter(lambda c: get_rid_of_number in c and all(
        #             i in self.number_set for i in c),
        #                 split_combinations))

        #     w = list(
        #         filter(lambda c: get_rid_of_number not in c
        #                 and one_in_list(c),
        #                 split_combinations))

        #     print(parent, v)
        #     print(parent, w)
        # print("k")

    def find_best_combination(self, no_lim):
        no_shrink = False
        if not no_shrink:
            max_mins = []
            while len(max_mins) < 1:
                split_number = self.numbers_to_choose_from[
                    randint(0, len(self.numbers_to_choose_from)-1)]
                split_combinations = self.cached_combinations.get(
                    split_number, set())

                valid_add_combinations = list(filter(lambda c: all(
                    i not in self.number_set for i in c), split_combinations))

                valid_remove_combinations = list(filter(lambda c: all(
                    i in self.number_set for i in c), split_combinations))

                if (not len(valid_add_combinations)
                        or not len(valid_remove_combinations)):
                    continue

                min_list_combo = self.random_extreme(
                    valid_remove_combinations, min)

                max_valid_combo = self.random_extreme(
                    valid_add_combinations, max)

                max_mins.append((len(max_valid_combo) - len(min_list_combo),
                                min_list_combo, max_valid_combo))

            mm_score = [i[0] for i in max_mins]

            if not no_lim:
                if max(mm_score) >= 0:
                    max_rand = list(filter(
                        lambda x: x[0] == max(mm_score), max_mins))

                    _, best_min, best_max = max_rand[
                        randint(0, len(max_rand)-1)]

                    self.number_set = self.number_set.difference(
                        set(best_min)).union(set(best_max))
                    no_shrink = True
            else:
                mm_score = [i[0] for i in max_mins]
                max_rand = list(filter(
                    lambda x: x[0] == max(mm_score), max_mins))

                _, best_min, best_max = max_rand[
                    randint(0, len(max_rand)-1)]

                self.number_set = self.number_set.difference(
                    set(best_min)).union(set(best_max))

    def find_fractions(self):
        self.best_combination = True
        for set_item in self.number_set.intersection(
                set(self.numbers_to_choose_from)):
            set_item_combinations = self.cached_combinations.get(set_item, [])

            set_item_combinations = list(filter(lambda c: all(
                i not in self.number_set for i in c), set_item_combinations))

            if not len(set_item_combinations):
                continue

            next_lists = [sum(len(self.cached_combinations.get(number, []))
                              for number in valid) / len(valid)
                          for valid in set_item_combinations]

            max_next_list = set_item_combinations[
                next_lists.index(max(next_lists))]

            self.number_set = self.number_set.difference(
                {set_item}).union(set(max_next_list))

            self.best_combination = False
            return

    def best_set_check(self):
        if len(self.best_set) < len(self.number_set):
            self.best_set = self.number_set.copy()
            if len(self.number_set) > 900:
                with open("lists.csv", "a") as writer:
                    writer.writelines(f"{str(len(self.number_set))}, "
                                      f"{str(datetime.utcnow())}, "
                                      f"{str(self.number_set)}\n")

            # f"Best list: {sorted(self.best_set)}"
            print(f"\nSum: {self.fraction_sum(self.best_set)}, "
                  f"Len: {len(self.number_set)}")

            print("Time:", datetime.utcnow())
        if self.count > 100:
            print(f"Recent list: "
                  f"Sum: {self.fraction_sum(self.number_set)}, "
                  f"Len: {len(self.number_set)}")
            print(f"Best list: "
                  f"Sum: {self.fraction_sum(self.best_set)}, "
                  f"Len: {len(self.best_set)}\n")
            self.count = 0

    def fraction_sum(self, lst):
        return round(sum(1/i for i in lst), 14)

    def main(self):
        self.count = 0
        print("Starting at:", datetime.utcnow())

        self.read_data()
        print("Data loaded.")

        while True:
            # t0 = time.time()
            self.best_set_check()
            # t1 = time.time()
            # print("\nbest_set_check()", t1-t0)
            # t0 = time.time()
            self.find_fractions()
            # t1 = time.time()
            # print("\nfind_fractions()", t1-t0)
            if self.best_combination:
                # t0 = time.time()
                self.removing_numbers_check()
                print(self.number_set)
                # self.replace_smartly()
                for i in range(11):
                    # print("working..")
                    self.find_fractions()
                    self.find_best_combination(no_lim=False)
                for i in range(1):
                    self.find_fractions()
                    self.find_best_combination(no_lim=True)
                print("len:", len(self.number_set),
                      "sum:", self.fraction_sum(self.number_set))
                # t1 = time.time()
                # print("\nfind_best_combination()", t1-t0)
                self.best_combination = False
                self.can_remove = {}
            self.count += 1


if __name__ == "__main__":
    model = FractionSumFinder([249, 254, 256, 262, 278, 284, 301, 318, 338, 344, 348, 350, 352, 363, 365, 369, 372, 374, 375, 377, 378, 381, 384, 385, 388, 390, 391, 395, 396, 399, 400, 402, 403, 406, 408, 410, 412, 414, 418, 420, 423, 425, 426, 429, 430, 432, 434, 435, 436, 437, 438, 440, 441, 442, 444, 445, 448, 450, 451, 455, 456, 459, 460, 462, 464, 465, 468, 470, 472, 473, 474, 476, 477, 480, 481, 483, 484, 485, 486, 488, 490, 492, 493, 494, 495, 496, 497, 500, 504, 506, 507, 508, 510, 511, 512, 513, 515, 516, 517, 518, 519, 520, 522, 524, 525, 527, 528, 530, 532, 533, 534, 536, 539, 540, 544, 546, 548, 549, 550, 551, 552, 555, 556, 558, 559, 560, 561, 564, 567, 568, 570, 572, 574, 575, 576, 578, 580, 581, 582, 583, 584, 585, 588, 589, 590, 592, 594, 595, 598, 600, 602, 603, 604, 605, 606, 608, 609, 611, 612, 615, 616, 618, 620, 621, 623, 624, 627, 630, 636, 637, 638, 639, 640, 642, 644, 645, 646, 648, 649, 650, 651, 654, 655, 656, 658, 660, 663, 664, 665, 666, 667, 670, 671, 672, 675, 676, 679, 680, 682, 684, 685, 686, 688, 689, 690, 693, 696, 697, 700, 702, 703, 704, 707, 708, 710, 711, 712, 713, 714, 715, 716, 720, 722, 725, 726, 728, 729, 730, 731, 732, 735, 736, 737, 738, 740, 741, 742, 744, 747, 748, 749, 750, 752, 754, 755, 756, 759, 760, 762, 765, 767, 768, 770, 774, 775, 776, 777, 779, 780, 781, 782, 783, 784, 785, 786, 790, 792, 793, 795, 798, 799, 800, 803, 804, 805, 806, 808, 810, 812, 814, 816, 817, 819, 820, 824, 825, 826, 828, 832, 833, 834, 835, 836, 837, 840, 845, 846, 847, 848, 850, 851, 852, 854, 855, 858, 860, 861, 864, 868, 869, 870, 871, 872, 873, 874, 876, 880, 882, 884, 885, 888, 889, 890, 891, 893, 894, 896, 897, 899, 900, 901, 902, 903, 906, 909, 910, 912, 913, 915, 917, 918, 920, 923, 924, 925, 927, 928, 930, 931, 935, 936, 938, 940, 943, 944, 945, 946, 948, 949, 950, 952, 954, 957, 959, 960, 962, 963, 966, 968, 969, 970, 972, 975, 976, 979, 980, 981, 984, 986, 987, 988, 989, 990, 992, 994, 996, 999, 1000, 1001, 1005, 1007, 1008, 1012, 1014, 1015, 1017, 1020, 1022, 1023, 1025, 1026, 1029, 1030, 1032, 1034, 1035, 1036, 1037, 1040, 1043, 1044, 1045, 1048, 1050, 1053, 1054, 1056, 1057, 1060, 1062, 1064, 1065, 1066, 1067, 1068, 1070, 1071, 1073, 1075, 1078, 1079, 1080, 1081, 1085, 1088, 1090, 1092, 1095, 1098, 1100, 1102, 1104, 1105, 1107, 1110, 1111, 1112, 1113, 1116, 1118, 1120, 1121, 1122, 1125, 1127, 1128, 1130, 1131, 1134, 1136, 1139, 1140, 1143, 1144, 1147, 1148, 1150, 1152, 1155, 1157, 1160, 1161, 1162, 1164, 1166, 1168, 1169, 1170, 1173, 1175, 1176, 1177, 1178, 1180, 1183, 1184, 1185, 1188, 1189, 1190, 1196, 1197, 1200, 1204, 1206, 1207, 1209, 1210, 1212, 1215, 1216, 1218, 1219, 1220, 1221, 1222, 1224, 1225, 1230, 1232, 1235, 1236, 1239, 1240, 1242, 1243, 1245, 1246, 1247, 1248, 1250, 1251, 1254, 1256, 1258, 1260, 1261, 1264, 1265, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1278, 1280, 1281, 1284, 1287, 1288, 1290, 1292, 1295, 1296, 1298, 1300, 1302, 1305, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1316, 1320, 1323, 1325, 1326, 1328, 1330, 1332, 1333, 1334, 1335, 1337, 1340, 1342, 1344, 1350, 1352, 1353, 1356, 1360, 1363, 1364, 1365, 1368, 1370, 1372, 1375, 1376, 1377, 1378, 1380, 1386, 1387, 1390, 1392, 1394, 1395, 1397, 1400, 1403, 1404, 1406, 1407, 1408, 1410, 1411, 1413, 1414, 1416, 1417, 1419, 1420, 1421, 1422, 1424, 1425, 1426, 1428, 1430, 1431, 1435, 1440, 1441, 1442, 1443, 1444, 1449, 1450, 1452, 1455, 1456, 1457, 1458, 1460, 1462, 1463, 1464, 1469, 1470, 1472, 1474, 1475, 1476, 1479, 1480, 1482, 1484, 1485, 1488, 1491, 1494, 1495, 1496, 1498, 1500, 1501, 1504, 1505, 1508, 1512, 1515, 1517, 1518, 1519, 1520, 1521, 1524, 1525, 1526, 1528, 1529, 1530, 1533, 1534, 1536, 1537, 1539, 1540, 1541, 1545, 1547, 1548, 1550, 1551, 1552, 1554, 1558, 1560, 1562, 1564, 1566, 1568, 1572, 1573, 1575, 1580, 1581, 1582, 1584, 1586, 1590, 1591, 1593, 1595, 1596, 1598, 1599, 1600, 1602, 1605, 1606, 1608, 1610, 1611, 1612, 1615, 1616, 1617, 1620, 1624, 1625, 1628, 1632, 1633, 1634, 1635, 1638, 1639, 1640, 1643, 1644, 1645, 1647, 1649, 1650, 1651, 1652, 1653, 1656, 1659, 1660, 1661, 1664, 1665, 1666, 1668, 1672, 1674, 1675, 1677, 1679, 1680, 1683, 1690, 1692, 1694, 1696, 1700, 1702, 1704, 1705, 1708, 1710, 1711, 1712, 1715, 1716, 1717, 1719, 1720, 1722, 1725, 1728, 1729, 1730, 1734, 1736, 1738, 1739, 1740, 1742, 1743, 1746, 1748, 1749, 1750, 1751, 1752, 1755, 1760, 1763, 1764, 1767, 1768, 1769, 1770, 1771, 1775, 1776, 1778, 1780, 1781, 1782, 1785, 1786, 1788, 1792, 1794, 1798, 1800, 1802, 1804, 1805, 1806, 1807, 1809, 1812, 1813, 1815, 1818, 1819, 1820, 1824, 1825, 1826, 1827, 1829, 1830, 1833, 1836, 1837, 1840, 1845, 1846, 1848, 1850, 1853, 1854, 1855, 1856, 1859, 1860, 1862, 1863, 1869, 1870, 1872, 1875, 1876, 1880, 1881, 1885, 1886, 1887, 1888, 1890, 1891, 1892, 1896, 1898, 1900, 1903, 1904, 1905, 1908, 1911, 1914, 1917, 1919, 1920, 1924, 1925, 1926, 1927, 1932, 1935, 1936, 1938, 1940, 1943, 1944, 1947, 1950, 1952, 1953, 1955, 1957, 1958, 1960, 1961, 1962, 1963, 1968, 1969, 1971, 1972, 1974, 1975, 1976, 1978, 1980, 1984, 1988, 1989, 1992, 1995, 1998, 2000, 2001, 2002, 2006, 2009, 2010, 2013, 2014, 2015, 2016, 2020, 2021, 2023],
                              "data_sorted.tom")
    model.main()
