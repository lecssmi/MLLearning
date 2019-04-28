
#直接使用seaborn绘图
import numpy as np

import  pandas as  pd

import matplotlib.pyplot as plt

import  seaborn as sns

text = np.genfromtxt("../../resources/02_knn/datingTestSet2.txt",delimiter="\t")

print(len(text))

features=np.zeros((1000,3),dtype=float)

labels=np.zeros((1000,1),dtype=int)

all=np.zeros((1000,4),dtype=float)




count=0

for line in text:

        features[count]=line[0:3]

        labels[count]=line[3]

        all[count]=line
        count+=1

#
# print(features)
#
# print(labels)


df = pd.DataFrame(data=features,columns=["x","y","z"])

df1 = pd.DataFrame(data=all, columns=["x", "y", "z", "l"])


pal={1:"green",2:"blue",3:"red"}

g = sns.FacetGrid(data=df1, hue="l", palette=pal,height=5,legend_out=True)

g.map(plt.scatter,"x","y",alpha=1,linewidth=0.5)

g.add_legend()

plt.show()






