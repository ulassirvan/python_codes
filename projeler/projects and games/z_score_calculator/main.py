import numpy as np

mean=50
sd=5
örnek_sayısı=10000000
x=-1.6

sayılar=np.random.normal(mean,sd,örnek_sayısı)
olasılık_degeri=mean+(sd*x)


sayılar=sayılar<olasılık_degeri
adet=np.count_nonzero(sayılar)

olasılık=adet/örnek_sayısı*100
print(olasılık)




