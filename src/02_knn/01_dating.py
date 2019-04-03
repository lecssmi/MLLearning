# 本文主要用于编写海伦约会配对数据
from numpy.matlib import zeros, array

import sys


# 将每一行数据的前三个作为特征，最后一个数字作为标签
def fileToMatrix(filename,value):
    fr = open(filename)
    length = len(fr.readlines())
    # returnMat = zeros((length, 3))

    returnMat=[[]]
    classLabelVector=[]

    fr=open(filename)
    index=0

    for line in fr.readlines():

        split = line.split("\t")

        if int(split[-1])==value:

            # returnMat[index]=split[0:3]

            returnMat[0].append(split[0:3])
            classLabelVector.append(int(split[-1]))



        index+=1

    return  returnMat,classLabelVector


if __name__ == '__main__':
    (mat1,classLabelVector1) = fileToMatrix("../../resources/02_knn/datingTestSet2.txt",1)
    #
    # print(classLabelVector)


    import matplotlib.pyplot as plt

    figure = plt.figure()
    ax = figure.add_subplot(111)

    # 将第一列的和第二列单独拿出来做对比，分别将对应不同z值的点化成不同的颜色
    # mat1=[]
    # label1=[]
    #
    # mat2=[]
    # label2=[]
    #
    # index =0
    # for x in mat[:,0]:
    #     if classLabelVector[index]==1:
    #         mat1.append(mat1)
    #         label1.append(classLabelVector[index])
    #     elif classLabelVector[index]==2:
    #         mat2.append()
    #
    #     index+=1
    #
    #
    #
    #
    # # 这里的x，y需要使用中括号括起来，不知道是为啥？API的变动？
    ax.scatter([mat1[:, 0]], [mat1[:, 1]],c="r")

    (mat2, classLabelVector2) = fileToMatrix("../../resources/02_knn/datingTestSet2.txt", 2)

    ax.scatter([mat2[:, 0]], [mat1[:, 2]],c="g")

    (mat3, classLabelVector3) = fileToMatrix("../../resources/02_knn/datingTestSet2.txt", 3)

    ax.scatter([mat3[:, 0]], [mat3[:, 2]], c="b")






    #
    plt.show()

#     todo 继续将图绘制完毕








