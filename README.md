## Explanation

Figurify is a Python library that allows you to perform various calculations related to geometric figures. With Figurify, you can quickly and easily calculate properties such as perimeter, area, angles, and more for various geometric shapes.

## Installation

You can easily install Figurify using pip:

    pip install figurify

## Supported Calculations

    material_properties
    units

Geometric Solids

    Cube
    Cuboid
    Cylinder
    Cone
    Sphere
    Torus
    Prism
    Pyramid

Plane Metrics

    Circle
    Rectangle
    Triangle
    Square
    Trapezoid
    Polygon
    Ellipse
    Parallelogram
    Quadrilateral

Figure Physics

    Dynamics
    Forces
    Energy
    Gravity
    Kinematics
    Momentum  

And there are many functions in every Python file.<br>
For more information about the available functions and figures, see the documentation.

## Bugs

We welcome contributions from other developers! If you've found a bug or want to add a new feature, feel free to create an issue or submit a pull request.<br>

## License

This project is licensed under the MIT License. See the license file for more information.


## Usage

Here's a simple example of how to use Figurify in your Python project:

```python
from figurify import *

# Calculate the circumference of a circle with a radius of 5
circumference = figurify.plane_metrics.circle.circumference(5)
print("Circumference of the circle:", circumference)

# Calculate the area of a rectangle with a length of 4 and a width of 3
area = figurify.plane_metrics.rectangle.area(4, 3)
print("Area of the rectangle:", area)

# And there's much more, see above.
