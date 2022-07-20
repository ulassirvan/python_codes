def isPrime(sayi):
    sayac=2;
    sum=0.0;
    while(sayac*sayac<=sayi):
        if sayi%sayac==0:
            if(sayac*sayac==sayi):
                sum+=sayac
            else:
                sum+=sayac+(sayi/sayac)
        sayac+=1
    sum+=1
    if sayi==sum:
        return True

i=0
primelist=[]
for i in range(1,100000000):
    if isPrime(float(i)):
        print(i)
    if i%1000000==0:
        print(str(i)+". sayiyi hesapladi")


print(primelist)


