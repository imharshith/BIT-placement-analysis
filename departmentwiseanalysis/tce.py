#BIT TCE department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
TCE_OFFERS=[36,41,24,31] 
TCE_ELIGIBLE=[38,47,32,32] 
TCE_PLACED=[34,39,23,29]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("TCE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,TCE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,TCE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,TCE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
