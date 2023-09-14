# a * x * x + b * x + c == 0 

def solve_quadratic(a: float, b: float, c: float) -> tuple:
    D = b**2 - 4*a*c
    if D < 0:
        return None
    
    x1 = (-b - D**(1/2))/(2 * a)
    x2 = (-b + D**(1/2))/(2 * a)

    if x1 == x2:
        return (x1, )

    result = (x1, x2)

    return result


res = solve_quadratic(a=1, b=4, c=1)
print(res)

assert solve_quadratic(1, 6, 5) == (-5, -1)
assert solve_quadratic(1, 4, 4) == (-2,)
assert solve_quadratic(1, 6, 45) is None
