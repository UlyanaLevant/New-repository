slovo = input('Введите любое из трех слов "погода","дата" или "шутка" : ')
if slovo == "погода":
    sz = input("Погода на завтра или на сегодня?: ")
    if sz == "на сегодня":
        print("Погода на сегодня 17 градусов")
    elif sz == "на завтра":
        print("Погода на завтра 22 градуса")
    else:
        print("Не то ввели")
elif slovo == "дата":
    data = input("Дата на сегодня или на завтра?: ")
    if data == "на сегодня":
        print("12.08.2021")
    elif data == "на завтра":
        print("13.08.2021")
    else:
        print('не то ввели')
elif slovo == "шутка":
    sh = input("Шутка на русском или на английском?: ")
    if sh == "на русском":
        smeh = input('Смешную или не смешную шутку на русском?: ')
        if smeh == "смешную":
            print("не знаю смешных шуток на русском")
        elif smeh == "2":
            print("Не смешные шутки это скучно")
        else:
            print('не то ввел')
    elif sh == "на английском":
        print("Шуток на английском тоже не знаю")
    else:
        print("не то ввели")

else:
    print('НУЖНО ВВЕСТИ ОДНО ИЗ ТРЕХ СЛОВ')
