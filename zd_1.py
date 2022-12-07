#Создайте программу для игры с конфетами человек против бота.
#Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
#a) Добавьте игру против бота

from random import *
import os
os.system('cls' if os.name == 'nt' else 'clear')

welcome_text = ('Приветствую Вас!\n'
                'Хотите сыграть в игру?\n'
                'Для начала я расскажу правила:\n'
                'Я даю Вам конфет, вы берете их поочереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                'Ну что начнем?')
print(welcome_text)

message = ['твоя очередь', 'да бери уже', 'бери больше']



def player_vs_bot():
    candies_total = 120
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()