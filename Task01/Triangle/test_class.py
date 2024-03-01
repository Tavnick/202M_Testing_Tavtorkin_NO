import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_triangle_creation():
    # Позитивные тесты
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.a == 3
    assert triangle1.b == 4
    assert triangle1.c == 5

    # Негативные тесты
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-2, 3, 2)

    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 4, 10)

def test_triangle_type():
    # Позитивные тесты
    triangle1 = Triangle(5, 5, 5)
    assert triangle1.triangle_type() == "equilateral"

    triangle2 = Triangle(5, 5, 4)
    assert triangle2.triangle_type() == "isosceles"

    triangle3 = Triangle(3, 4, 5)
    assert triangle3.triangle_type() == "nonequilateral"

def test_triangle_perimeter():
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.perimeter() == 12

    triangle2 = Triangle(5, 5, 5)
    assert triangle2.perimeter() == 15

    triangle3 = Triangle(5, 5, 4)
    assert triangle3.perimeter() == 14

if __name__ == "__main__":
    pytest.main()