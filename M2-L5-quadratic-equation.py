# a * x * x + b * x + c == 0 

def solve_quadratic(a: float, b: float, c: float) -> tuple:
    D = b**2 - 4*a*c
    if D < 0:
        return None
    
    x1 = (-b + D**(1/2))/2
    x2 = (-b - D**(1/2))/2

    if x1 == x2:
        return (x1, )

    result = (min(x1, x2), max(x1, x2))

    return result


res = solve_quadratic(a=1, b=4, c=1)
print(res)


