def circumference(radius):
    return 2 * radius * custom_pi()

def area(radius):
    return radius**2 * custom_pi()

def diameter(radius):
    return radius * 2

def radius(diameter):
    return diameter / 2

def arc_length(radius, angle):
    return radius * angle

def sector_area(radius, angle):
    return (radius**2 * angle) / 2

def chord_length(radius, angle):
    return 2 * radius * custom_sin(angle / 2)

def inscribed_angle(arc_length, radius):
    return arc_length / radius

def central_angle(arc_length, radius):
    return arc_length / radius

def apothem(radius, side_length):
    return radius - custom_sqrt(radius**2 - (side_length / 2)**2)

def sector_angle(sector_area, radius):
    return (sector_area * 2) / radius**2

def segment_area(radius, chord_length):
    return (radius**2 / 2) * (custom_asin(chord_length / (2 * radius)) - custom_sin(custom_asin(chord_length / (2 * radius))))

def custom_pi():
    return 3.14159

def custom_sin(x):
    return x - x**3 / 6 + x**5 / 120 - x**7 / 5040

def custom_asin(x):
    return x + x**3 / 6 + 3 * x**5 / 40 + 5 * x**7 / 112
