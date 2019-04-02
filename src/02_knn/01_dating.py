# 本文主要用于编写海伦约会配对数据
from numpy.matlib import zeros

import sys


def fileToMatrix(filename):
    fr = open(filename)
    length = len(fr.readlines())
    returnMat = zeros((length, 3))
    classLabelVector=[]

    fr=open(filename)
    index=0

    for line in fr.readlines():
        split = line.split("\t")

        returnMat[index,:]=split[0:3]

        classLabelVector.append(int(split[-1]))

        index+=1

    return  returnMat,classLabelVector


if __name__ == '__main__':
    (mat,classLabelVector) = fileToMatrix("../../resources/02_knn/datingTestSet2.txt")


    import matplotlib.pyplot as plt

    figure = plt.figure()
    ax = figure.add_subplot(111)








