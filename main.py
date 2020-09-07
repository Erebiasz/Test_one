weapon=["Nożyczki","Kamień","Papier"]
suma_1=0
suma_2=0
while suma_1 !=3 and suma_2 !=3  :
    Player_1 = str(input("Player one choose your weapon: "))
    Player_2 = str(input("Player two choose your weapon: "))
    if Player_1 and Player_2  in weapon:
        print("oks")
    else: print("Zła broń")
    if Player_1==Player_2:
        print("Remis")
    elif Player_1==("Kamień") and Player_2==("Nożyczki"):
        print("Wygrał Player 1")
        suma_1 +=1
    elif Player_1==("Nożyczki") and Player_2==("Papier"):
        print("Wygrał Player 1")
        suma_1 += 1
    elif Player_1==("Papier") and Player_2==("Kamień"):
        print("Wygrał Player 1")
        suma_1 += 1
    elif Player_2==("Kamień") and Player_1==("Nożyczki"):
        print("Wygrał Player 2")
        suma_2 += 1
    elif Player_2==("Nożyczki") and Player_1==("Papier"):
        print("Wygrał Player 2")
        suma_2 += 1
    elif Player_2==("Papier") and Player_1==("Kamień"):
        print("Wygrał Player 2")
        suma_2 += 1
    print("Wynik : ",suma_1," ",suma_2)
    suma_1=int(suma_1)