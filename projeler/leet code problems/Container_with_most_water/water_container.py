
en_büyük_alan=[0,0,0]
def water_container_calculator(sayılar):
    i=0
    p=len(sayılar)-1
    max_area=0
    while p>i:
        if max_area<(min(sayılar[p],sayılar[i])*(p-i)):
            max_area=(min(sayılar[p],sayılar[i])*(p-i))

        if min(sayılar[p],sayılar[i])==sayılar[p]:
            p -= 1
        else:
            i += 1

    print(f"max area: {max_area}")

water_container_calculator([1,8,6,2,5,4,8,3,7])





