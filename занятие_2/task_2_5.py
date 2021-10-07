rub = int(input("Введите количество рублей: "))
kop = int(input("Введите количество копеек: "))
if rub == 1:
    if kop == 1:
        print(rub, "рубль", kop, "копейка")
    elif kop > 1 and kop < 5:
        print(rub, "рубль", kop, "копейки")
    elif kop == 0 or kop > 4:
        print(rub, "рубль", kop, "копеек")
elif rub > 1 and rub < 5:
    if kop == 1:
        print(rub, "рубля", kop, "копейка")
    elif kop > 1 and kop < 5:
        print(rub, "рубля", kop, "копейки")
    elif kop == 0 or kop > 4:
        print(rub, "рубля", kop, "копеек")
elif rub == 0 or rub > 4:
    if kop == 1:
        print(rub, "рублей", kop, "копейка")
    elif kop > 1 and kop < 5:
        print(rub, "рублей", kop, "копейки")
    elif kop == 0 or kop > 4:
        print(rub, "рублей", kop, "копеек")


