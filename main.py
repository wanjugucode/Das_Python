import csv
from figure import MergeSort
from search import SearchCSV
from Trees import UpdateCSV
from setuptools import find_packages, setup

import pdb
def search_csv (file_name,  price):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        tree = UpdateCSV()
        node = tree.buildTree(data, price)
        print(tree.csvPrice(node))
        print(tree.minPrice(node))
setup(
    name="scripts",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.6",
    install_requires =["Click"],
    entry_points={
        'console_scripts':["command_line = scripts.command_line:main"]
    }
)