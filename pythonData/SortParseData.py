class systemSort:
    def sortCSV_NameFile():
        with open('./CSV_NameFile.txt', 'r') as CSV_ReadFIle:
            data = CSV_ReadFIle.read().replace(".", "\n")
            newFile = open("refinedData.txt", "w")
            newFile.write(data)

    def fileDisplay(): #Print just numbers
        with open("./refinedData.txt", "r") as tempNumbers:
            pass

if __name__ == "__main__":
    mainExecute = systemSort
    mainExecute.sortCSV_NameFile()
    mainExecute.fileDisplay()