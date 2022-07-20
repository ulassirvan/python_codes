import numpy as np
import matplotlib.pyplot as plt

bin=np.arange(50,100)
erkekler=np.random.normal(69.1,2.9,1000)
kadılar=np.random.normal(63.7,2.7,1000)


plt.hist(erkekler,bins=30,histtype="bar",stacked=True,rwidth=0.5,range=(55,80),alpha = 0.95)
plt.hist(kadılar,bins=30,histtype="bar",stacked=True,rwidth=0.5,range=(55,80),alpha = 0.75)
plt.show()


