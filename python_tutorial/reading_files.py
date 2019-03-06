import sys


#working with txt files
with open("entyFile.txt") as entryFile:
    for row in entryFile:
        column = row.split(',')
        num1 = int(column[1])
        num2 = int(column[2])
        total += num1 + num2
        print(" num 1: {}, Num2: {}, Total: {}".format(num1,num2, total))

#working with .csv
import csv
total = 0
with open("testcsv.csv") as csvFile:
    for i, row in enumerate(csv.reader(csvFile)): #i can use the enumerate to convert the list in a enumerable object in order to have the index element
        num1 = int(row[1])
        num2 = int(row[2])
        total += num1 + num2
        print(" num 1: {}, Num2: {}, Total: {}".format(num1,num2, total))
print("total rows {}".format( i))