
# 词云
from PIL import Image

f = open("../../resources/02_knn/words",encoding="utf-8")

text=f.read()

f.close()



from wordcloud import WordCloud as wc

import  numpy as np

mask = np.array(Image.open("1.jpg"))

cloud = wc(background_color="white", width=1000, height=100, margin=2,mask=mask).generate(text)

import matplotlib.pyplot as plt

plt.imshow(cloud)

plt.axis("off")

plt.show()

cloud.to_file("./demo.jpg")


print(mask.shape)

