import model
from create_bot import bot
from aiogram import types


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет! '
                                                 f'Сегодня будем делить конфеты. '
                                                 f'Основные правила игры: '
                                                 f'Нам будет дано 150 конфет, '
                                                 f'за один шаг мы можем взять не более 28 конфет. '
                                                 f'Побеждает тот, кто заберет последнюю конфету. Итак, начнём! '
                                                 f'выбери уровень сложности: /level 0 - легкий, /level 1 - сложный.')


