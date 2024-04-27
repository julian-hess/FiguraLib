def area(radius):
	value = 3.14159 * radius**2
	return value

def circumference(radius):
	value = 2 * 3.14159 * radius
	return value

def diameter(radius):
	value = 2 * radius
	return value

def radius(area):
	value = (area / 3.14159) ** 0.5
	return value

def radius_from_circumference(circumference):
	value = circumference / (2 * 3.14159)
	return value

def area_from_circumference(circumference):
	value = (circumference**2) / (4 * 3.14159)
	return value

def circumference_from_diameter(diameter):
	value = 3.14159 * diameter
	return value