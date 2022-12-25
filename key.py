from random import *
# блок генератора ключа

def key(number):
    block1 = ''  # создаю строчку
    for i in range(5):
        block1 += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'[randint(0, len('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') - 1)]
        #генерирую рандомный символ из списка всех
        block = block1 + '-'  #
        temp = block1.replace(block1[randint(0, len(block1) - 1)], '', 1)
    for i in range(3):
        if i == 2:
            number = int(number) % 10  # беру модуль третьей цифры
            temp = temp[number:] + temp[:number]
            block += temp  # на третьем круге цикла '-' не нужно
        elif i == 0:
            number = (int(number) // 100) % 10  # беру модуль первой цифры
            temp = temp[number:] + temp[:number]
            block += temp + '-'  # в первый и третий сдвиг двигаю одинакого
        elif i == 1:
            number = (int(number) // 10) % 10  # беру модуль второй цифры
            temp = temp[-number:] + temp[:-number]
            block += temp + '-'   #двигаю не туда куда в первый раз
        temp = temp.replace(temp[randint(0, len(temp) - 1)], '', 1)   # убираю 1 символ
    return block
