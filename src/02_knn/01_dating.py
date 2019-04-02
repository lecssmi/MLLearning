# 本文主要用于编写海伦约会配对数据
from numpy.matlib import zeros, array

import sys


# 将每一行数据的前三个作为特征，最后一个数字作为标签
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
    #
    # print(classLabelVector)


    import matplotlib.pyplot as plt

    figure = plt.figure()
    ax = figure.add_subplot(111)

    # 将第一列的和第二列单独拿出来做对比，分别将对应不同z值的点化成不同的颜色
    mat1=[]
    label1=[]

    index =0
    for x in mat[:,0]:
        if classLabelVector[index]==1:
            mat1.append(mat1)

    # 这里的x，y需要使用中括号括起来，不知道是为啥？API的变动？
    ax.scatter([mat[:, 0]], [mat[:, 1]],cmap=classLabelVector)

    plt.show()

#     todo 继续将图绘制完毕








