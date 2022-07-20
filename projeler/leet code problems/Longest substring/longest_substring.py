


def substring(metin):
    metin.lower()
    i=0
    j=1
    longest_string=0
    chars=[]
    while True:


        if j==(len(metin)):
            break
        if not metin[j] in chars:
            chars.append(metin[j])
            j+=1
            print(f"j:{j}")
        else:
            print(f"j:{j}")
            i,j = j,j+1
            chars=[]
            print(f"j:{j}")


        if longest_string<len(metin[i:j]):
            longest_string=len(metin[i:j])

    return longest_string

metin="abcdef"
print(substring(metin))
print(len(metin))


