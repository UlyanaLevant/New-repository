sent = input("Введите предложение: ")
x = len(sent)
if x % 3 == 0:
    print(sent, "!")
elif x % 3 > 0:
    print("Число символов в предложении не кратно трем")
