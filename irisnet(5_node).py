#To load a new dataset,
#replace csv filename, change the columns,
#(lines 32,33,34) and adjust number of epochs.(94)
#             -Gage

import csv
iris = open('iris.csv', "rb")
reader = csv.reader(iris, delimiter = ',')

data = []

for row in reader:
    data.append(row)



#define weights
weight_n4 = 1
weight_n5 = 1

#open files containing data



l = 1
#50 for iris, 25 for gen,
#change n1, 2, and 3 for different models
def netrun():
    #input var1 and var2 and varif by
    #changing the number in the second bracket set
    sepal_length = float(data[l][0])
    sepal_width = float(data[l][1])
    petal_width = float(data[l][2])





    n2 = (sepal_width + sepal_length) / 2
    n1 = sepal_length - sepal_width
    n3 = sepal_length + sepal_width

    n4 = ((n1 * weight_n4) + (n2 * weight_n4)) / 2
    n5 = ((n2 * weight_n5) + (n3 * weight_n5)) / 2

    print n4, n5


    n4_potweight = (petal_width - n4) / petal_width
    n5_potweight = (petal_width - n5) / petal_width

    if n4 > petal_width:
        global weight_n4
        weight_n4 = weight_n4 - (weight_n4 - n4_potweight) / (weight_n4 * 25)

    else:
        global weight_n4
        weight_n4 = weight_n4 + (weight_n4 - n4_potweight) / (weight_n4 * 25)

    if n5 > petal_width:
        global weight_n5
        weight_n5 = weight_n5 - (weight_n5 - n5_potweight) / (weight_n5 * 25)

    else:
        global weight_n5
        weight_n5 = weight_n5 + (weight_n5 - n5_potweight) / (weight_n5 * 25)

    global l
    l += 1




def FinalTest():
    testlength = input('Sepal Length = ')
    testwidth = input('Sepal Width = ')

    n2 = (testwidth + testlength) / 2
    n1 = testlength - testwidth
    n3 = testlength + testwidth

    n4 = ((n1 * weight_n4) + (n2 * weight_n4)) / 2
    n5 = ((n2 * weight_n5) + (n3 * weight_n5)) / 2

    print n4, n5






for x in range(0,49):
    netrun()


print weight_n4, weight_n5

FinalTest()
