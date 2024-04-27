def area(semi_major_axis, semi_minor_axis):
    return semi_major_axis * semi_minor_axis * custom_pi()

def perimeter(semi_major_axis, semi_minor_axis):
    return 2 * semi_major_axis * custom_pi() + 4 * (semi_minor_axis - semi_major_axis)

def focal_distance(semi_major_axis, semi_minor_axis):
    return custom_sqrt(semi_major_axis**2 - semi_minor_axis**2)

def eccentricity(semi_major_axis, semi_minor_axis):
    return focal_distance(semi_major_axis, semi_minor_axis) / semi_major_axis

def vertex_distance(semi_major_axis, semi_minor_axis):
    return custom_sqrt(semi_major_axis**2 - semi_minor_axis**2)

def semi_latus_rectum(semi_major_axis, semi_minor_axis):
    return semi_major_axis * (1 - eccentricity(semi_major_axis, semi_minor_axis)**2)

def linear_eccentricity(semi_major_axis, semi_minor_axis):
    return custom_sqrt(semi_major_axis**2 - semi_minor_axis**2)

def co_vertex_distance(semi_major_axis, semi_minor_axis):
    return custom_sqrt(semi_major_axis**2 - semi_minor_axis**2)

def focus_distance(semi_major_axis, semi_minor_axis):
    return 2 * semi_major_axis

def major_axis_length(semi_major_axis, semi_minor_axis):
    return 2 * semi_major_axis

def minor_axis_length(semi_major_axis, semi_minor_axis):
    return 2 * semi_minor_axis

def semi_major_axis_length(major_axis_length):
    return major_axis_length / 2

def semi_minor_axis_length(minor_axis_length):
    return minor_axis_length / 2

def custom_pi():
    return 3.14159

def custom_sqrt(x):
    return x ** 0.5
