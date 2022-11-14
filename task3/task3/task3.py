import csv
import os
import shutil

with open('students.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if not os.path.exists(row[0]): os.makedirs(row[0])
            line_count += 1

dir_src = "data/"
dir_dst1 = "Tutorials"
dir_dst2 = "Games"
for filename in os.listdir(dir_src):
    if filename.endswith('.pdf'):
        shutil.move(dir_src+filename,dir_dst1)
    elif filename.endswith('game'):
        shutil.move(dir_src+filename,dir_dst2)