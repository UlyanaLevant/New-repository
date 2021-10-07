a = 3
b = 8
for i in range(a, b+1):
    for j in range(1,i):
        if i%j != 0:
            print(i)
