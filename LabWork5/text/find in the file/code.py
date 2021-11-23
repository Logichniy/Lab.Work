import csv
import sys
print("Пошук даних у файлі")
filename = "LabWorkZ.txt"
line = str(input())
fd = open(filename, "r")
fd1 = fd.readlines()
for row in fd1:
    if line in row:
        print(row)