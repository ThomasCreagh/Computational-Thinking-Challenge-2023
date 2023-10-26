def find_fractions_to_add(fraction):
    num, denom = fraction

    results = []
    for d in range(2, 2024):
        for n in range(1, d):
            if num * d == denom * n + denom:
                results.append((n, d))

    return results


print(find_fractions_to_add((1, 4)))
