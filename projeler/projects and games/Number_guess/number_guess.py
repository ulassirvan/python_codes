import random

def user_guees():
    return int(input("Guess one number"))

print("welcome to number guess game")
print("number is betwen 1 and 100")
if (input("Oyun modu seçın (Hard,easy)").lower()=="hard"):
    remaning_guess=5
else:
    remaning_guess=10

rasgale_sayı=random.randint(1,100)
print(f"rasgele sayı {rasgale_sayı}")
while remaning_guess>0:
    tahmin=user_guees()
    if tahmin == rasgale_sayı:
        print(f"You are corecct number is {rasgale_sayı}")
        break
    else :
        print("youre number incorecct. ")
        if tahmin<rasgale_sayı:
            print("random number is biger than your guess")
        else:
            print("random number is smaller than your guess")

    remaning_guess-=1
    print(f"remaning guess:{remaning_guess}")


print(f"value of random number{rasgale_sayı}")

