import csv
import json


# Reading the CSV #
with open('sample.csv', 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')

    # List of entries without whitespaces #
    temp = [{key: val for key, val in i.items() if key != ''} for i in csv_reader]

with open('sample.json', 'w') as f:
    json.dump(temp, f, sort_keys=True, indent=3)