def count_ways():
    ways = [[0] * (800 + 1) for _ in range(2023 - 2 + 1)]

    # Initialize first row with zeros except first element
    ways[0][0] = 1

    # Compute number of ways for each row and column
    for i in range(1, 2023 - 2 + 1):
        for j in range(i, 800 + 1):
            for k in range(2, i + 1):
                if j >= int(1 / k):
                    ways[i][j] += ways[i - 1][j - int(1 / k)]

    # Return number of ways to form sum of 1 with all 800 rational numbers
    return ways[2023 - 2][800]

print(count_ways())