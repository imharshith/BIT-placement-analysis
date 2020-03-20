#BIT ITE(INDUSTRIAL Engg. and MANAGEMENT) department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
ITE_OFFERS=[34,28,18,18] 
ITE_ELIGIBLE=[36,26,31,31] 
ITE_PLACED=[25,26,17,16]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("ITE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,ITE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ITE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,ITE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
