import csv

def testFunctionRead():

    with open ("/doneProjects/Python/pythonData/MOCK_DATA.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:

            if line_count == 0:
                print(f'coulmn names are {",".join(row)}')
                line_count += 1

            else:
                fileWrite = open('CSV_NameFile.txt', 'a')
                fileWrite.write(f"\t{row[0]} works in the {row[1]}.")
                fileWrite.close()
                line_count += 1

testFunctionRead()