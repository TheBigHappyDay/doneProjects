import numpy
import matplotlib.pyplot as plt
import random

class learningML:

    def __init__(self, result, SDarray):
        result = []
        SDarray = []
        self.result = result
        self.SDarray = SDarray

    def main(self):

        #Makes a 0 -> 99 random INT array ranging from 1 -> 150
        for _ in range (100):
            RNum = random.randint(1, 150)
            self.SDarray.append(RNum)

        #Finding and printing all INTs in the Array SDarray and the SD
        self.result = numpy.std(self.SDarray)
        print(f"ALL NUMS -> {self.SDarray}")
        print("----------------------------")
        print(f"SD -> {round(self.result, 2)}")

    def graphFunction(self):

        #Setting font classes
        font1 = {'family':'Arial', 'color':'black', 'size':'15'}
        font2 = {'family':'Arial', 'color':'black', 'size':'10'}
        
        #Calling the SDarray to now be a local variable
        x = numpy.array(self.SDarray)

        #Making the graph
        plt.plot(x, marker = 'o', ms = 5, ls = ':')
        plt.title("Standard Deviation", fontdict=font1)
        plt.ylabel("INT Weight", fontdict=font2)
        plt.xlabel("INT Spread", fontdict=font2)
        plt.grid()

        plt.show()

#Calling functions from the class
mainProg = learningML(0, 0)
mainProg.main()
mainProg.graphFunction()