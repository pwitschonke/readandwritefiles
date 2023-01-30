import csv

with open('EmployeePay.csv', 'r') as inputFile:
    inputFile = csv.reader(inputFile, delimiter=',')

    next(inputFile)

    for i in inputFile:
        print(f"{i[0]:5s} {i[1]:15s} {i[2]:15s} {i[3]:15s} {i[4]:15s}")
