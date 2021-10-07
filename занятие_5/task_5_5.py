group = 20
sher_1 = ''
sher_2 = ''
sher_3 = ''
sher_4 = ''
for i in range(1, group + 1, 4):
    sher_1 += str(i) + ", "
    sher_2 += str(i + 1) + ", "
    sher_3 += str(i + 2) + ", "
    sher_4 += str(i + 3) + ", "
print(f' 1 шеренга: {sher_1}\n 2 шеренга: {sher_2}\n 3 шеренга: {sher_3}\n 4 шеренга: {sher_4}\n')
