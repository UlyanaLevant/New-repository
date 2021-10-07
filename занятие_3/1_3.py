chel = "тартарары"
print(chel.split("р"))
print(chel.find("а"))
print(chel.rfind("а"))
print(chel.count("а"))  # количество подстрок в строке
print(chel.replace("а", "у"))  # первая - что менять, вторая - на что менять
print(len(chel))  # так можно узнать длину строки
print("{} {} {}".format(3, 5, 7))
print("{1} {0} {2}".format(3, 5, 7))  # можно форматировать строку в порядке индексации
print("{1} {0} {2}".format(5 + 3, "safast".split("s"), 7 * 3))
print(f"{4} буквы {chel * 3}")
print(chel.upper())  # длает всю строку большими


# a = "рено"
# b = "внимательность"
# print(a[2::-1]+a[3:4]+b[:2]+b[10:])
