
#直接使用seaborn绘图
import numpy as np

import  pandas as  pd

import matplotlib.pyplot as plt

import  seaborn as sns

def getFeatures():
        text = np.genfromtxt("../../resources/02_knn/datingTestSet2.txt", delimiter="\t")

        print(len(text))

        features = np.zeros((1000, 3), dtype=float)

        labels = np.zeros((1000, 1), dtype=int)

        all = np.zeros((1000, 4), dtype=float)

        count = 0

        for line in text:
                features[count] = line[0:3]

                labels[count] = line[3]

                all[count] = line
                count += 1

        #
        # print(features)
        #
        # print(labels)


        df = pd.DataFrame(data=features, columns=["x", "y", "z"])

        df1 = pd.DataFrame(data=all, columns=["x", "y", "z", "l"])

        # pal = {1: "green", 2: "blue", 3: "red"}

        # g = sns.FacetGrid(data=df1, hue="l", palette=pal, height=5, legend_out=True)
        #
        # g.map(plt.scatter, "x", "y", alpha=1, linewidth=0.5)
        #
        # g.add_legend()

        # plt.show()

        return all




# 到这里，知道了以x,y为特征能够比较好的分类
# 计算每个点的之间的距离

def calDistance(x, y, all):
        dis = np.zeros(1000, dtype=float)

        # print(dis)

        maxdis=[]
        count=0
        for line in all:
                distance= ((x-line[0])**2+(y-line[1])**2)**0.5

                maxdis.append([distance,count])

                count+=1


        return maxdis





if __name__ == '__main__':

        all=getFeatures()

        max = calDistance(80000,10, all)

        df=pd.DataFrame(max,columns=["distance","index"])

        # print(df.head())

        sort = df.sort_values("distance", ascending=True)

        # print(sort.head())

        head = sort.head(10)

        # print(head)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        index = head["index"]
        # print(index)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



        for  inx in index:

                print(all[inx][3])
















