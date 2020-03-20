#BIT placement analysis for the academic year 2015

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

plt.rcParams['figure.figsize']=(15,5)

style.use('ggplot')

BRANCH=['CSE','ECE','ISE','TCE','EEE','ITE','ME','CVE','EIE']
OFFERS=[126,125,59,36,53,34,113,42,31] 
ELIGIBLE=[110,127,43,38,49,36,105,101,28] 
PLACED=[93,110,43,34,43,25,82,38,26]

xpos=np.arange(len(BRANCH))
#print(xpos)

plt.xticks(xpos,BRANCH)
plt.title("BIT PLACEMENT ANALYSIS 2015")
plt.xlabel("BRANCH")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
