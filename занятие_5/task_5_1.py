slovo = input("Введите слово: ")
a = 0
while slovo not in ('стоп', 'хватит', 'достаточно'):
    a += 1
    slovo = input("Введите слово: ")
print(a)