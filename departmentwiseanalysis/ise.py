#BIT ISE department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
ISE_OFFERS=[59,51,42,47] 
ISE_ELIGIBLE=[43,49,39,39] 
ISE_PLACED=[43,46,35,33]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("ISE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,ISE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ISE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,ISE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
