num = int(input('Введите натуральное число: '))
stroka = input('Введите строку: ')
str_1 = ''
num_1 = 0
while num != num_1:
    num_1 += 1
    stroka += '*'
    str_1 += stroka
    stroka = input('Введите строку: ')
    if num_1 == num:
        print(str_1.split('*'))

# не понимаю, как разделить введенные слова, они склеиваются без пробела
# а через звездочку появляется пустая строчка в списке


































































