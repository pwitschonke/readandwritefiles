import csv

with open('EmployeePay.csv', 'r') as inputFile:
    inputFile = csv.reader(inputFile, delimiter=',')

    next(inputFile)

    print("ID    First Name      Last Name       Salary           Bonus           Total Pay")

    for i in inputFile:
        iden = i[0]
        fName = i[1]
        lName = i[2]
        salary = i[3]
        bonus = i[4]
        totalPay = float(i[3]) * (1 + float(i[4]))

        print(
            f"{i[0]:5s} {i[1]:15s} {i[2]:15s} ${i[3]:15s} {i[4]:15s} ${round(totalPay,2)}", end='')

        input()
