from fractions import Fraction


def to_frac(v):
    v = Fraction(v)
    v = v.limit_denominator(1000)
    v = str(v)
    if "/" in v:
        v = v.split("/")
        v = "\\frac{%s}{%s}" % (v[0], v[1])
    return v


print(to_frac(8/9))
