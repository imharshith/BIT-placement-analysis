#BIT CSE department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
CSE_OFFERS=[126,135,184,164] 
CSE_ELIGIBLE=[110,109,142,142] 
CSE_PLACED=[93,100,133,124]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("CSE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,CSE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,CSE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,CSE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
