# Добавьте игру против бота
import random


def player_step():
    try:
        while True:
            num = int(input('Возьми конфеты: '))
            if 0 < num < 29:
                break
            else:
                print('Мухлюешь')
        return num
    except:
        print('Это не число!')


def bot():
    step = random.randint(1, 28)
    return step


name_1 = input('Введите имя: ')
name_2 = input('Введите имя БОТА : ')
lot = random.randint(1, 2)
amount = int(input("Введите количество конфет : "))
while True:
    print(f'Осталось {amount} конфет(ы). Можешь взять от 1 до 28 конфет')
    if lot == 1:
        step_1 = player_step()
        amount -= step_1
        lot = 2
    else:
        step_2 = bot()
        amount -= step_2
        print(f'{name_2} взял {step_2}')
        lot = 1
    if amount < 1:
        if lot == 1:
            print('Game over')
        else:
            print('Ура-победа!')
        break
