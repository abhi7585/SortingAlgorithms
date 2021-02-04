import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="SortingAlgorithms",
    version="1.0",
    description="This package will help user to get the results of few sorting algorithms.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abhi7585/SortingAlgorithms",
    author="Abhishek Tripathi",
    author_email="abhi.workonly@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=["SortingAlgorithms"],
    include_package_data=True,
    install_requires=[],
)
