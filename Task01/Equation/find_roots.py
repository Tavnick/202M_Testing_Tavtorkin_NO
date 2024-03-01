import math

def find_roots(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return []
            else:
                return []
        else:
            return [-c / b]
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return sorted([x1, x2])
        elif discriminant == 0:
            x = -b / (2*a)
            return [x]
        else:
            return []