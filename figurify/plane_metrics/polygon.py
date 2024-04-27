def perimeter(s):
    return sum(s)

def area(s, a):
    return sum(s) * a / 2

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

def semiperimeter(s):
    return sum(s) / 2

def side_length_from_perimeter(p, n):
    return p / n

def side_length_from_area(a, ap):
    return 2 * a / ap

def num_sides_from_perimeter(p, s):
    return p / s

def num_sides_from_area(a, ap):
    return 2 * a / ap
