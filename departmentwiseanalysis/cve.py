#BIT CVE department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
CVE_OFFERS=[42,39,18,17] 
CVE_ELIGIBLE=[101,94,97,97] 
CVE_PLACED=[38,30,17,15]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("CVE DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,CVE_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,CVE_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,CVE_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
