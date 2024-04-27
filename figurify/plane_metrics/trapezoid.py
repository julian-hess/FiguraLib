def area(base1, base2, height):
    return (base1 + base2) * height / 2

def perimeter(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

def height(area, base1, base2):
    return 2 * area / (base1 + base2)

def side_length(area, base1, base2, height):
    return 2 * area / height - base1 - base2

def base_midline(base1, base2):
    return (base1 + base2) / 2

def side_from_perimeter(perimeter, base1, base2, side2):
    return perimeter - base1 - base2 - side2

def base_from_perimeter(perimeter, side1, side2, height):
    return perimeter - side1 - side2 - 2 * height

def side_from_area(area, base1, base2, height):
    return 2 * area / (height + base1 + base2)

def angle_at_base(base1, base2, side1, side2):
    return 180 - interior_angle(4) - angle_at_top(base1, base2, side1, side2)

def angle_at_top(base1, base2, side1, side2):
    return 180 - angle_at_base(base1, base2, side1, side2)

def diagonal(base1, base2, height):
    return (base1 - base2)**2 + height**2

def side_diagonal(base1, base2, side1, side2, height):
    return (base1 - base2)**2 + side1**2 - 2 * (base1 - base2) * side1 * custom_cos(3.14159 - angle_at_top(base1, base2, side1, side2))

def base_diagonal(base1, base2, side1, side2, height):
    return (base1 - base2)**2 + side1**2 - 2 * (base1 - base2) * side1 * custom_cos(3.14159 - angle_at_base(base1, base2, side1, side2))

def interior_angle(n):
    return (n - 2) * 180 / n

def apothem(s, n):
    return s / (2 * custom_tan(3.14159 / n))

def custom_tan(x):
    return custom_sin(x) / custom_cos(x)

def custom_sin(x):
    return x - x**3 / 6 + x**5 / 120 - x**7 / 5040

def custom_cos(x):
    return 1 - x**2 / 2 + x**4 / 24 - x**6 / 720
