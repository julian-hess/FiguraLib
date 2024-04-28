from setuptools import setup, find_packages

setup(
    name='figurify',
    version='0.1',
    author='Julian Hess',
    description='With figurify you can calculate figures, surfaces and physics.',
    long_description='Figurify is a Python library that allows you to perform various calculations related to geometric figures.'
                     ' With Figurify, you can quickly and easily calculate properties such as'
                     ' perimeter, area, angles, and more for various geometric shapes.',
    url='https://github.com/julian-hess/Figurify.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
