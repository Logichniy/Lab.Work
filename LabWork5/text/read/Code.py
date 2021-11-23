import csv
import sys
print("Group 1")
filename = "LabWorkZ.txt"
fd = open(filename, "r")
reader=csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)
print("Group 2")
filename = "LabWorkZ.txt"
fd = open(filename, "r")
reader=csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)