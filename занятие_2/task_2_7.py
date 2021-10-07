user_input = input("Введите пожалуйста номер месяца: ")
month = int(user_input)
if month == 1:
    print("В январе 31 день")
elif month == 2:
    print("В феврале 28 дней")
elif month == 3:
    print("В марте 31 день")
elif month == 4:
    print("В апреле 30 дней")
elif month == 5:
    print("В мае 31 день")
elif month == 6:
    print("В июне 30 дней")
elif month == 7:
    print("В июле 31 день")
elif month == 8:
    print("В августе 31 день")
elif month == 9:
    print("В сентябре 30 дней")
elif month == 10:
    print("В октябре 31 день")
elif month == 11:
    print("В ноябре 30 дней")
elif month == 12:
    print("В декабре 31 день")
else:
    print("Вы ввели некорректный номер меясца")