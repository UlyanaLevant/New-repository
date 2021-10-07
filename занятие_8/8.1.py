A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 1, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# if sum(A) > sum(B):
#     print('Сумма больше в кортеже - A')
# else:
#     print('Сумма больше в кортеже - B')
# print('Минимельный элемент в кортеже А -', A.index(min(A)))
# print('Минимельный элемент в кортеже B -', B.index(min(B)))

# Русская рулетка  (не могу добавить введенные имена в кортеж, чтоб потом вывести одно оттуда)
import random

number = int(input('Введите количество игроков: '))
guesses = 1
print('Стрельба началась')
name = input('Имя игрока: ')
while guesses < number:
    name = input('Имя игрока: ')
    tuple_1 = tuple(name)
    guesses += 1
while guesses == number:
    guess = random.randint(0, number + 1)
    dog = int(input('Крутите барабан (число от 1 до 6): '))
    if dog > guess:
        print('Вы не попали, попробуйте ее раз!')
    if dog < guess:
        print('Вы не попали, попробуйте ее раз!')
    if dog == guess:
        print('В яблочко! Вы убили -', tuple_1[dog])
        break

