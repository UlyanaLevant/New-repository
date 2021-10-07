# 1
# vor = "каркаркаркаркаркаркаркаркаркар"
# print(vor.count("кар"))
#
# # 2
# sl = "малако, каровы, харашо"
# print(sl.replace("а", "о"))
#
# # 3
# sms = input("Введите смс: ")
# a = len(sms)
# if a % 60 > 0:
#     print(a // 60 + 1, "sms")
# elif a % 60 == 0:
#     print(a / 60, "sms")

# 4
# a = "БОЛЬШОЙ БАРЬЕРНЫЙ РИФ"
# b = "маленькийпринц"
# print(a.isupper())
# print(b.islower())

# 5
# str = input('Введите строку: ')
# str = str.casefold()
# if 'вверх' in str:
#     print(str.upper())
# elif 'вниз' in str:
#     print(str.lower())
# else:
#     print(str)

# # 6
# mus = input("Введите слово 'музыка': ")
# mus = mus.casefold()
# if mus == "музыка":
#     print(("Тыц\n тЫц\n тыЦ\n ") * 3, ":)")
# else:
#     print("Вы ввели другое слово")

#7
passworld = input("Введите пароль (минимум 8 символов, буквы обоих регистров, минимум одна цифра и символ): ")
passworld2 = input('Повторите пароль: ')
if " " in passworld:
    print("Нельза вводить пробелы")
elif len(passworld) < 8:
    print("Недостаточно симвалов")



