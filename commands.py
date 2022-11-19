import asyncio
from create_bot import dp
import random
import model
from aiogram import types
from create_bot import bot


async def start(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await bot.send_message(message.from_user.id, f'{player.first_name}, привет! '
                                                 f'Сегодня будем делить конфеты. '
                                                 f'Основные правила игры: '
                                                 f'Нам будет дано {model.total_candies} конфет, '
                                                 f'за один ход мы можем взять не более {model.max_take} конфет. '
                                                 f'Побеждает тот, кто заберет последнюю конфету. Итак, начнём!')
    await asyncio.sleep(3)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)    
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)
     

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player_id(player)
    if (message.text).isdigit():
        if 0 < int(message.text) < 29:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял {player_take} конфет, '
                                              f'и на столе осталось {total} конфет.')
            if model.check_win(total): 
                await bot.send_message(player.id, f'Победил {player.first_name}')
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await bot.send_message(message.from_user.id, 'А не многовато ли взял?')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                     f'Вообще-то мы конфеты считаем в цифрах')

async def enemy_turn(player):
    total_count = model.get_total_candies()
    if total_count < 29:
        enemy_take = total_count
    else:
        enemy_take = (total_count - 1) % 28
    total = total_count - enemy_take
    model.set_total_candies(total)
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, '
                                      f'и на столе осталось {total} конфет.')
    if model.check_win(total): 
        await bot.send_message(player.id, f'Победил {player.first_name} ты проиграл, '
                                          f'тебя дёрнула железяка')
        return
    
    await asyncio.sleep(1)
    await await_player(player)



async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id,
                            f'{player.first_name}, бери конфеты, но не больше {max_take}')


async def set_total_candies(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимальное количество конфет изменили на '
                                                 f'{count}')