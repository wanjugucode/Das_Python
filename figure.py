import csv
from cmd import MergeSort
from search import SearchCSV

import pdb
def search_csv (file_name, target, finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        things = SearchCSV(data,target, finder)
        things.search()
        print(things)
    pdb.set_trace()
search_csv("agency-real-estate.csv", '229096452', 'code')