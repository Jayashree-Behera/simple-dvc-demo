# This is  a python file which is used download packages
# or create your own package. The package you make can be
# seen using cmd line "pip freeze" andcan be imported too

from setuptools import setup, find_packages

setup(
    name = "src", # name of your package
    version = "0.0.1",
    description = "its a wine q package",
    author = "Shree",
    packages = find_packages(),
    license="MIT"
    )