#BIT placement analysis for the academic year 2017

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

plt.rcParams['figure.figsize']=(15,5)

style.use('ggplot')

BRANCH=['CSE','ECE','ISE','TCE','EEE','ITE','ME','CVE','EIE']
OFFERS=[184,132,42,24,28,18,45,18,15] 
ELIGIBLE=[142,175,39,32,47,31,104,97,24] 
PLACED=[133,125,35,23,26,17,41,17,14]

xpos=np.arange(len(BRANCH))
#print(xpos)

plt.xticks(xpos,BRANCH)
plt.title("BIT PLACEMENT ANALYSIS 2017")
plt.xlabel("BRANCH")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
