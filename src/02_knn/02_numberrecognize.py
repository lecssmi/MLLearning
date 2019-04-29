
# 手写数字识别

# 1.因为数字是32*32的，且有内容的地方为1，没有内容的地方为0，可以将每一个图片转换成32*32=1024的一行向量。

import pandas as pd
import  numpy as np


def  img2vectors(dir):

    import os
    files = os.listdir(dir)
    matrix = np.zeros(size=(len(files), 1024))

    labels=np.zeros(size=len(files))

    count=0
    for file in files:
        tupe = file.split(".")[0]
        label = tupe.split("_")[0]

        labels[count]=int(label)

        input = open(file, encoding="utf-8")

        for i in range(32):

            line = input.readline()

            for j in range(32):

                matrix[count,count*i+j]=int(line[j])

            count+=1


    return matrix,labels

# 将测试数据和训练数据进行比较，看测试的准确度.

def testDataPredict(testDir,matrix,labels):

    import  os

    files = os.listdir(testDir)

    for file in files:
        label=file.split(".")[0].split("_")[0]


        vector=np.zeros(size=1024)
        input = open(file)

        for i in range(32):
            line=input.readline()

            for j in range(32):

                vector[32*i+j]=int(line[j])

        result = calDistance(vector, matrix, labels)

# TODO 如果result里面的结果，和自带的label不匹配，那就是有问题的地方。这种算法太朴素


def calDistance(vector1,matrix,labels):

    distances=np.zeros(len(labels,2))

    for x in range(matrix.shape(0)):

        vector2=matrix[x,:]

        sum=0

        for i in range(1024):

            sum=sum+vector1[i]**2+vector2[i]**2




        distances[x,0]=sum**0.5

        distances[x,1]=labels[x]

    df = pd.DataFrame(data=distances, columns=["distance", "label"]).sort_values("distance",ascending=False).head(3)
    return df





if __name__ == '__main__':
    vectors,labels = img2vectors("trainData")

    testDataPredict("testDir",vectors,labels)












