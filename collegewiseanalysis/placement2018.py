#BIT placement analysis for the academic year 2018

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

plt.rcParams['figure.figsize']=(15,5)

style.use('ggplot')

BRANCH=['CSE','ECE','ISE','TCE','EEE','ITE','ME','CVE','EIE']
OFFERS=[164,150,47,31,37,18,59,17,15] 
ELIGIBLE=[142,175,39,32,47,31,104,97,24] 
PLACED=[124,112,33,29,34,16,55,15,14]

xpos=np.arange(len(BRANCH))
#print(xpos)

plt.xticks(xpos,BRANCH)
plt.title("BIT PLACEMENT ANALYSIS 2018")
plt.xlabel("BRANCH")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
