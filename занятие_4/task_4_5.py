n = int(input("Введите натуральное число: "))
for i in range(1,n+1):
    if n+1 < 6:
        print(i, end=" ")
    elif n+1 > 6 and n+1 <= 11:
        for j in range(1,6):
            print(j)
