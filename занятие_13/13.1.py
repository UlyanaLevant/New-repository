# list_1 = ['Петрова', 'Сидоров', 'Панамаренка', 'Пахипко']
# for i in list_1:
#     if i[0] == 'П'and i[-1] == 'а':
#         print(i)
# list_2 = []
# for i in list_1:
#     list_2.append(i[::-1])
# print(list_2)
# n = 0
# dict_1 = {}


# pupils = [
#     {'firstname': 'Masha',
#      'Group': 42,
#      'physics': 7,
#      'informatics': 6,
#      'history': 8,
#      },
# ]
# pupils.append({'firstname': 'Natasha',
#      'Group': 42,
#      'physics': 8,
#      'informatics': 4,
#      'history': 7,
#      })
# pupils.append({'firstname': 'Kolya',
#      'Group': 42,
#      'physics': 4,
#      'informatics': 2,
#      'history': 9,
#      })
# # n = 0
# for value in pupils[0].values():
#     if value is not int:
#         continue
#     else:
#         if value < 10:
#             n += 1
#             print(value/n)


spisok_1 = [
    {'Car_1': 'Nisan',
     'number': 12345,
     'year': 1994},
    {'Car_1': 'Tayota',
     'number': 43215,
     'year': 2001},
    {'Car_1': 'Audi',
     'number': 55542,
     'year': 2014}
]
spisok_2 = []
for i in spisok_1:
    for key, value in i.items():
        if key == 'year' and value > 2000:
            print(value)

