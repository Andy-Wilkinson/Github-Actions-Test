import pathlib
from setuptools import setup, find_packages
from ghactionstest.__version__ import __version__

# The directory containing this file
here = pathlib.Path(__file__).parent

# Read files for inclusion in the setup
readme = (here / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ghactionstest",
    version=__version__,
    description="A GitHub actions test package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Andy-Wilkinson/Github-Actions-Test",
    author="Andrew Wilkinson",
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
)
