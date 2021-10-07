# Умножить bruce_willis на пятый элемент строки, введенный пользователем

bruce_willis = 42
input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = bruce_willis * leeloo
except ValueError:
    print("Введите число!")
except IndexError:
    print('Вы вышли за границы списка!')
else:
    print(f"- Leeloo Dallas! Multi-pass № {result}!")


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

