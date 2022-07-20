def unit_vector(vector_1:list,vector_2:list):
    """
    :param vector_1: x , y , z valuse of vector 1
    :param vector_2: x , y , z valuse of vector 2
    :return: return the unit vector of given input vector1 to vector2
    """
    if (len(vector_1)!=2 and len(vector_1)!=3) or(len(vector_2)!=2 and len(vector_2)!=3):
        print("verilen vektorler 2 boyutlu veya 3 boyutlu olmalı")
        return False
    if len(vector_1)!=len(vector_2):
        print("vectorler aynı boyutta olmalı")
        return False
    else:
        vector=[]
        for i in range(len(vector_1)):
            vector.append(vector_1[i]-vector_2[i])
        sum=0
        for i in vector:
            sum+=i**2

        sum **= 1 / 2
        for i in range(len(vector)):
            vector[i] /= sum

    return vector

print("arrow on vector 1")
vector1= [float(input("vector1 x: ")), float(input("vector1 y: ")), float(input("vector1 z: "))]
vector2= [float(input("vector2 x: ")), float(input("vector2 y: ")), float(input("vector2 z: "))]

print(unit_vector(vector1,vector2))

