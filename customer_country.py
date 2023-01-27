import csv

with open('customers.csv', 'r') as inputFile:
    inputFile = csv.reader(inputFile)

    with open("customer_country.csv", "w", newline='') as outputFile:
        outputFile = csv.writer(outputFile)

        for line in inputFile:
            outputFile.writerow([line[1], line[2], line[4]])
