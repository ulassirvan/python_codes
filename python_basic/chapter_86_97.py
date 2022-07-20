onbir_bolum_0=[]
for i in (range(0,100)):
    if i%11==0:
        onbir_bolum_0.append(i)

print(onbir_bolum_0)

onbir_üç_bolum_0=[]
for i in (range(0,100)):
    if i%11==0 and (not(i%3==0)):
        onbir_üç_bolum_0.append(i)

print(onbir_üç_bolum_0)


items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
iki_ile_bolum=[]
for i in items:
    if i%2==0:
        iki_ile_bolum.append(i)


print(iki_ile_bolum)


items = [1, 5, 3, 2, 2, 4, 2, 4]
not_duplicate=[]
for i in items:
    if not i in not_duplicate:
        not_duplicate.append(i)

print(not_duplicate)


text = 'Python is a very popular programming language'
kelimeler=[]
for i in range(0,4):
    kelimeler.append(text.split(" ")[i].lower())

print(kelimeler)

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
prob=[]


for i in probabilities:
    if i >0.5:
        prob.append(i)


print(prob)


probabilities2 = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

for i in range(len(probabilities2)):
    if probabilities2[i]>0.5:
        probabilities2[i]=1
    else:
        probabilities2[i]=0


print(probabilities2)


items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
values={}
for i in items :
    if i in values.keys():
        values[i] += 1
    else:
        values[i] =1
print(values)


text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""


words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 6]
print(words)


indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]

hisseler=[]

for i in indexes:
    if "DOW"in i or "S&P"in i:
        hisseler.append(i)


print(hisseler)


gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}



for i in gaming:
    if gaming[i]>100:
        print(i)




names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']


for i in names:
    if i.isalpha():
        print(f"hellllooooooo {i} ....")


