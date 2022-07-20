list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break

print(result)



hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

for i in hashtags:
    if type(i)!="str":
        print(False)
        break


sayı =11

if sayı>1:
    for i in range(2,sayı):
        if sayı%i==0:
            print("asal sayı degıi")
            break
    else:
        print(f'{sayı} - prime number')
else:
    print("asal sayı degıi")



gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}



for i in gaming:
    if(gaming[i][1]=="PLN"):
        continue
    else:
        gaming[i][1]="PLN"
        gaming[i][0] *= 4


print(gaming)


names = ['Jack', 'Leon', 'Alice', None, 'Bob']


for name in names:
    if name is None:
        continue
    print(name)