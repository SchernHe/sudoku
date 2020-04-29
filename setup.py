from distutils.core import setup

INSTALL_REQUIRES = [
    "pandas",
    "numpy",
]

setup(
    name="sudoku",
    version="1.0",
    author="Hendrik Scherner",
    packages=["sudoku"],
    install_requires=INSTALL_REQUIRES,
)