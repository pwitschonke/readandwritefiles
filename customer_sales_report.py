import csv

with open('sales.csv', 'r') as inputFile:
    inputFile = csv.reader(inputFile)

    with open("salesreport.csv", "w", newline='') as outputFile:
        outputFile = csv.writer(outputFile)

        outputFile.writerow(["CustomerID", "Total"])
        next(inputFile)

        for line in inputFile:
            outputFile.writerow(
                [line[0], round((float(line[3]) + float(line[4]) + float(line[5])), 2)])
