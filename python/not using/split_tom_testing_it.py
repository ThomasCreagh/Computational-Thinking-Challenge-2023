import random
from datetime import datetime

class FractionSumFinder:
    def __init__(self, number_list, file_name):
        self.number_set = set(number_list)
        self.original_set = set(number_list)
        self.file_name = file_name
        self.cached_combinations = {}
        self.fraction_list = []
        self.counter = 0
        self.index = 0
        self.done = True

    def read_data(self):
        with open(self.file_name, "r") as f:
            data = f.readlines()
            for line in data:
                number, combination_list = line.strip().split(":")
                number = int(number)
                combination_list = tuple(map(int, combination_list.split(", ")))

                if number in self.cached_combinations:
                    self.cached_combinations[number].add(combination_list)
                else:
                    self.cached_combinations[number] = {combination_list}

    def find_best_combination(self):
        mm_score = []
        max_mins = []
        while len(mm_score) < 5:
            split_number = random.randint(2, 2023)
            split_combinations = self.cached_combinations.get(split_number, set())
            if not split_combinations:
                continue

            def is_subset(c):
                return c.issubset(self.number_set)

            def is_disjoint(c):
                return c.isdisjoint(self.number_set)

            valid_combinations = set(filter(is_subset, split_combinations))
            if not valid_combinations:
                continue

            min_list_combo = min(valid_combinations, key=len)
            max_valid_combo = max(valid_combinations, key=len)

            max_mins.append((min_list_combo, max_valid_combo))
            mm_score.append(len(max_valid_combo) - len(min_list_combo))

        if not mm_score:
            return []

        best_min, best_max = max_mins[max(mm_score)]
        return self.number_set.difference(best_min).union(best_max)

    def find_fractions(self, number_set):
        if not number_set:
            return []

        if len(number_set) == 1:
            return list(number_set)

        max_sum = 1 / min(number_set)
        for number in sorted(number_set, reverse=True):
            if 1 - sum(self.fraction_list) < number / max_sum:
                continue

            self.fraction_list.append(number)
            new_set = number_set.difference({number})
            result = self.find_fractions(new_set)
            if result:
                return result

            self.fraction_list.pop()

        return []

    def main(self):
        # def is_disjoint(c):
        #     return c.isdisjoint(self.number_set)
        print("Starting at:", datetime.utcnow())
        print("Current best list: {}, Sum: {}".format(self.number_set,
                                                      sum(self.number_set)))
        self.read_data()
        print("Data loaded.")

        best_set = set()
        while True:
            if len(best_set) < len(self.number_set):
                best_set = self.number_set.copy()
                print("New best list: {}, Sum: {}".format(list(best_set),
                                                          sum(best_set)))
            if len(self.number_set) > 899:
                with open("lists2.csv", "a") as f:
                    f.write("{}, {}, {}\n".format(len(self.number_set),
                                                  datetime.utcnow(),
                                                  list(self.number_set)))

            for index in self.number_set:
                self.index = index
                combinations = self.cached_combinations.get(index, set())
                valid_combinations = set(filter(lambda c: c.isdisjoint(self.number_set), combinations))

                if not valid_combinations:
                    continue

                next_sums = [sum(len(self.cached_combinations.get(n, set())) for n in combo) / len(combo) for combo in valid_combinations]
                max_next_sum_idx = max(range(len(next_sums)), key=lambda i: next_sums[i])
                max_combination = valid_combinations[max_next_sum_idx]
                self.number_set.remove(index)
                self.number_set |= max_combination
                self.number_set = sorted(self.number_set)

                if len(self.number_set) > 890:
                    self.counter += 1
                if self.counter > 9999:
                    self.done = False
                    break

                fraction_sum = sum(1 / x for x in self.number_set)
                print(f"{self.counter}\t{round(fraction_sum, 14)}\t{len(self.number_set)}\t{datetime.utcnow()}")

            if self.done:
                new_set = self.find_best_combination()
                if new_set:
                    self.number_set = new_set
                    self.done = False
                else:
                    self.number_set = self.find_fractions(self.original_set)
                    if not self.number_set:
                        print("No solutions found.")
                        break
                    self.done = False

                    print("Finished at:", datetime.utcnow())
                    print("Best set: {}, Sum: {}".format(list(best_set), sum(best_set)))
                    with open("result.csv", "w") as f:
                        f.write("{}, {}\n".format(list(best_set), sum(best_set)))


if __name__ == "__main__":
    model = FractionSumFinder([2, 3, 6], "data.tom")
    model.main()
