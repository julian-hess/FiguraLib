from setuptools import setup, find_packages
import pathlib

setup(
    name='figurify',
    version='0.1',
    author='Julian Hess',
    description='With figurify you can calculate figures, surfaces and physics.',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url='https://github.com/julian-hess/Figurify.git',
    packages=find_packages(),
    project_urls={
        "Source": "https://github.com/julian-hess/Figurify.git"
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ],
)
