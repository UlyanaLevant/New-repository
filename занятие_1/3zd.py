try:
    ch_1 = input("Ведите первое дробное число: ")
    ch_2 = input("Введите второе дробное число: ")
    zn = input("Введите знак: ")
    if zn == "+":
        rec1 = float(ch_1) + float(ch_2)
        print(rec1)
    elif zn == "-":
        rec2 = float(ch_1) - float(ch_2)
        print(rec2)
    elif zn == "*":
        rec3 = float(ch_1) * float(ch_2)
        print(rec3)
    elif zn == "/":
        if ch_2 !=0:
            try:
                print(float(ch_1) / float(ch_2))
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
    else:
        print("Это неправильный знак")
except ValueError:
    print('Нельзя вводить строки!')
