import csv
import os
import random

with open('students.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)
    random_number = random.randint(1,len(data)-3)
    print(data[random_number])
    del data[random_number]
    out_str = str(data)
    csv_file.close()