import csv
import sys
print("Пошук даних у каталозі.")
filename = "LabWorkZ.txt"
line0 = int(input())
line = open(filename).readlines()[line0]
print("\n"+line)