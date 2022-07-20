import data

# TODO: entering coin foction
def enter_coin():
    cents_25=int(input("25 cent adeti: "))
    cents_10=int(input("10 cent adeti: "))
    cents_5=int(input("5 cent adeti: "))
    cents_1=int(input("1 cent adeti: "))
    return (cents_25*25)+(cents_10*10)+(cents_5*5)+(cents_1)


# TODO: ask user for type of coffe
while True:
    seçim=input ("What would you like? (e for espresso/l for latte/c for cappuccino):")
    if seçim=="e":
        print("pleas enter coins")
        seçim="espresso"
    elif seçim =="l":
        print("latte seçtiniz")
        seçim="latte"
    elif seçim=="c":
        print("cappuccino seçtiniz")
        seçim="cappuccino"
    elif seçim=="info":
        print("info seçtiniz")
        seçim="info"
    elif seçim=="off":
        break

    print(f"seçim: {seçim}")
    if seçim in data.MENU.keys():
        girlen_para = enter_coin()
        print(f"girdiginiz para: {girlen_para} ")
        if girlen_para>(data.MENU[seçim]["cost"]*100):
            print("para yeterli")
        else :
            print("para yetersiz")
    else :
        print(data.resources)







# TODO: check if is given coins sum is equal or greater than coffe price
