from numba import jit


@jit
def _sum(a, b):
    return sum((a, b))


print(_sum(1, 3))
