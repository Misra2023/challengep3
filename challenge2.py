def two_positive(a, b, c):
    return sum([num > 0 for num in (a, b, c)]) == 2
