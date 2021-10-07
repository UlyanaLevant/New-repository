number = 0
price_2 = 0
o_price = 0
money = int(input("Баланс вашго счета составляет: "))
price = int(input("Введите цену товара: "))
while money != 0:
    price_2 += price
    if price_2 <= money:
        number += 1
        price = int(input("Введите цену товара: "))
        o_money = money - price_2
    elif price_2 > money:
        print("остаток на счету", o_money)
        break
print(f"Общая стоимость - {money-o_money} рубл(я,ей), количество покупок - {number}")