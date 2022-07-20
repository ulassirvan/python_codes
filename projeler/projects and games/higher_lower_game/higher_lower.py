import data
import random

oyun_devam_ediyor_mu=True
your_score=0


def sık_yazıcı(sayı):
    print(f"name: {data.data[sayı]['name']}, {data.data[sayı]['description']} from {data.data[sayı]['country']}")

print(data.logo)

sık_a=random.randint(0,(len(data.data)-1))


while oyun_devam_ediyor_mu:
    print("             A: ")
    sık_yazıcı(sık_a)
    print(data.vs)
    sık_b=random.randint(0,(len(data.data)-1))
    print("             B: ")
    sık_yazıcı(sık_b)
    cevap=input("A is (higer/lower) than B")
    if cevap.lower()=="higer":
        if data.data[sık_a]["follower_count"]>data.data[sık_b]["follower_count"]:
            print("True, follower A is greater than B")
            your_score+=1
        else :
            print("False ")
            oyun_devam_ediyor_mu=False
    else:
        if data.data[sık_b]["follower_count"]>data.data[sık_a]["follower_count"]:
            print("True, follwer B is greater than A")
            your_score += 1
        else:
            print("False ")
            oyun_devam_ediyor_mu = False
    sık_b,sık_a=sık_a,sık_b

print(f"your score:{your_score}")