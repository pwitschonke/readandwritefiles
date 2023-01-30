import csv

with open('sales.csv', 'r') as inputFile:
    inputFile = list(csv.reader(inputFile))

    ID = inputFile[1][0]
    total = 0

    print(ID)

    with open("salesreport.csv", "w", newline='') as outputFile:
        outputFile = csv.writer(outputFile)

        outputFile.writerow(["CustomerID", "Total"])

        for i in range(1, len(inputFile)):
            if ID == inputFile[i][0]:
                newTotal = float(
                    inputFile[i][3]) + float(inputFile[i][4]) + float(inputFile[i][5])
                total += newTotal

            else:
                outputFile.writerow([inputFile[i-1][0]] +
                                    [str(round(total, 2))])
                ID = inputFile[i][0]
                total = 0
                newTotal = float(
                    inputFile[i][3]) + float(inputFile[i][4]) + float(inputFile[i][5])
                total += newTotal

            if i == len(inputFile) - 1:
                outputFile.writerow([inputFile[i][0]] + [str(round(total, 2))])
