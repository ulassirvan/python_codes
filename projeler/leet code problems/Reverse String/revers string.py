


def string_ters_çevirici(metin):
    metin=list(metin)
    i=0
    j=len(metin)-1
    temp=""
    while i<=j:
        print(i)
        print(j)
        temp=metin[j]
        metin[j]=metin[i]
        metin[i]=temp
        i+=1
        j-=1
    return str(metin)
print(string_ters_çevirici("hello"))