"""
setup python file
"""

import setuptools

setuptools.setup(
    name="csl",
    version="0.0.1",
    description="Scientific Library System",
    packages=setuptools.find_packages("src"),
    package_data={"": "src"},
)
