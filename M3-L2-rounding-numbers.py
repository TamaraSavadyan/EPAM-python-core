
def rounding_numbers(a: float, b: float) -> float:
    res = (12 * a + 25 * b) / (1 + a**(2**b))
    return round(res, 2)


res = rounding_numbers(2, 3)
print(res)
