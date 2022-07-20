with open("chapter_110_117\stock.txt","r") as dosya:
    metin=dosya.read().splitlines()
close=[]
for idx, line  in enumerate(metin):
    if idx>0:
        close.append(int(line.split(",")[-2]))


print(sum(close)/len(close))


with open("chapter_110_117\coin_pair.txt") as dosya:
    metin=dosya.read().splitlines()


pairs=[]

for pair in metin:
    if "USD" in pair:
        pairs.append(pair)


print(pairs)



with open('chapter_110_117\price.csv', 'r') as file:
    content = file.read().splitlines()

content.remove("Date,Open,High,Low,Close,Volume")
degerler={"close":[],"time":[]}
for i in content:
    degerler["close"].append(i.split(",")[-2])
    degerler["time"].append(i.split(",")[0])


print(degerler)



with open('chapter_110_117\price.csv', 'r') as file:
    content = file.read().splitlines()

content.remove("Date,Open,High,Low,Close,Volume")
max=0
tarih=""
for i in range(len(content)):
    if max<int(content[i].split(",")[-1]):
        max=int(content[i].split(",")[-1])
        tarih=content[i].split(",")[0]


print(max)
print(tarih)

iki_ile_olum=[]

for i in range(19):
    if i%2==0:
        iki_ile_olum.append(i)

print(iki_ile_olum)


with open("chapter_110_117/num.txt","w")as dosya:
    dosya.writelines(str(iki_ile_olum))

