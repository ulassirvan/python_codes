import numpy as np
import matplotlib.pyplot as plt
def flip_coin():
    return np.random.randint(0,2)
liste=[]
sayaç=0
for i in np.arange(100000):
    x=flip_coin()
    while x==1:
        if x ==1 :
            sayaç+=1
        else:
            break
        x=flip_coin()
    while x==0:
        if x ==0 :
            sayaç-=1
        else:
            break
        x=flip_coin()
    liste.append(sayaç)
    sayaç=0


plt.hist(liste)
plt.show()


print(liste)






print(np.count_nonzero(np.array(liste)))