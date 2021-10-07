# 2. Есть словарь координат городов

# sites = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480),
# }

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

# distances = {}
#
# distances['Moscow-London'] = (sites['Moscow'][0] - sites['London'][0])**2 + (sites['Moscow'][1] - sites['London'][1])**2
# distances['Paris-London'] = (sites['London'][0] - sites['Paris'][0])**2 + (sites['London'][1] - sites['Paris'][1])**2
# distances['Moscow-Paris'] = (sites['Moscow'][0] - sites['Paris'][0])**2 + (sites['Moscow'][1] - sites['Paris'][1])**2
# print(distances)

# 3. Есть словарь кодов товаров

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }

# Есть словарь списков количества товаров на складе.

# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1][
#     'quantity'] * store[goods['Стол']][1]['price']
# sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + store[goods['Диван']][1][
#     'quantity'] * store[goods['Диван']][1]['price']
# chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1][
#     'quantity'] * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2][
#                  'price']
# print('Лампа -', store[goods['Лампа']][0]['quantity'], 'шт, стоимость', lamps_cost, 'руб')
# print('Стол -', store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1][
#     'quantity'], 'шт, стоимость', table_cost, 'руб')
# print('Диван -', store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1][
#     'quantity'], 'шт, стоимость', sofa_cost, 'руб')
# print('Стул -', store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1][
#     'quantity'] + store[goods['Стул']][2]['quantity'], 'шт, стоимость', chair_cost, 'руб')


#3. в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов0+
# garden_set.update(meadow_set)
# print(garden_set)

# выведите на консоль те, которые растут и там и там
# print(meadow_set.intersection(garden_set))

# выведите на консоль те, которые растут в саду, но не растут на лугу
# print(garden_set.difference(meadow_set))

# выведите на консоль те, которые растут на лугу, но не растут в саду
print(meadow_set.difference(garden_set))











