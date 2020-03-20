#BIT ECE department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
ECE_OFFERS=[125,130,132,150] 
ECE_ELIGIBLE=[127,131,175,175] 
ECE_PLACED=[110,111,125,112]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("ECE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,ECE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ECE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,ECE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
