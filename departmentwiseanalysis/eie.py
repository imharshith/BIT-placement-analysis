#BIT EIE(ELECTRONICS & INSTRUMENTATION Engg.) department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
EIE_OFFERS=[31,21,15,15] 
EIE_ELIGIBLE=[28,19,24,24] 
EIE_PLACED=[26,17,14,14]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("EIE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,EIE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,EIE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,EIE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
