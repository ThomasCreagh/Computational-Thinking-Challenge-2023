from itertools import combinations

import time
start_time = time.time()

arr = [i for i in range(2, 20)]
k = 3

for i in combinations(arr, k):
    # print(i)
    pass


print("--- %s seconds ---" % (time.time() - start_time))
