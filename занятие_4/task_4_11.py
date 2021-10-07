a = int(input('Введите число: '))
Fib_2 = Fib_1 = 1
print(Fib_1)
for i in range(1, a+1):
    Fib_1, Fib_2 = Fib_2, Fib_1 + Fib_2
    print(Fib_2)














