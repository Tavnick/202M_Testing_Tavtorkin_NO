
class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    Возвращает тип треугольника, основанный на длинах его сторон.

    Параметры:
    a (float): Длина первой стороны.
    b (float): Длина второй стороны.
    c (float): Длина третьей стороны.

    Возвращает:
    str: Тип треугольника: "nonequilateral", "isosceles", "equilateral".

    Исключения:
    IncorrectTriangleSides: Если указанные длины сторон не могут образовать правильный треугольник.
    
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(5, 5, 4)
    'isosceles'
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    """
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise IncorrectTriangleSides("Incorrect sides of a triangle")
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()