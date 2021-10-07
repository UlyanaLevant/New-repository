# file_1 = open('byron.txt')
# for line in file_1:
#     print(line, end="")
# file_1.close()

# f = open('input.txt', mode = 'w')
# f.write(input())
# f.close()

# f = open('byron.txt', mode='r')
# print(f.readline())
# for i, line in enumerate(f):
#     if i == 4:
#         print(line)
# for i, line in enumerate(f):
#     if i < 5:
#         print(line)
# s_1 = int(input())
# f.close()

class InOutBlock:

    def __enter__(self):
        print('Входим в блок кода')
        # TODO обратите внимание что тут надо вернуть обьект - в видео это пропущено
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выходим из блока кода')

    def some_method(self):
        print('Выполяем метод обьекта InOutBlock')


with InOutBlock() as in_out:
    # in_out = InOutBlock()
    print('Некоторый код')
    in_out.some_method()

