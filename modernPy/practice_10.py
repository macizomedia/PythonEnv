import csv 

from typing import NamedTuple, DefaultDict, List, Dict
from pprint import pprint

with open('TSLA.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    head = next(iter(csv_reader))
    for row in csv_reader:
        print(head)
