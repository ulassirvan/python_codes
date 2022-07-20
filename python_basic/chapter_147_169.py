import numpy as np
def file_gen(data):
    for i in data:
        if i[-4:]==".txt":
            print(i)

file_gen(["file.txt","abdsd.csv","asdasd.jpg","sadasd.txt"])


ondan_buyuk=0
toplam_zar_atıs=0
for i in range(10000):
    toplam=np.random.randint(1, 7)+np.random.randint(1,7)
    if(toplam>10):
        ondan_buyuk+=1
    toplam_zar_atıs+=1
print(ondan_buyuk/toplam_zar_atıs)

omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f'Probability: {len(sum_gt_10) / len(omega):.2f}')


