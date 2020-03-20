#BIT placement analysis for the academic year 2016

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

plt.rcParams['figure.figsize']=(15,5)

style.use('ggplot')

BRANCH=['CSE','ECE','ISE','TCE','EEE','ITE','ME','CVE','EIE']
OFFERS=[135,130,51,41,43,28,89,39,21] 
ELIGIBLE=[109,131,49,47,48,26,124,94,19] 
PLACED=[100,111,46,39,33,26,54,30,17]

xpos=np.arange(len(BRANCH))
#print(xpos)

plt.xticks(xpos,BRANCH)
plt.title("BIT PLACEMENT ANALYSIS 2016")
plt.xlabel("BRANCH")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
