from create_bot import bot
from aiogram import types


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет! '
                                                 f'Сегодня будем делить конфеты. '
                                                 f'Основные правила игры: '
                                                 f'Нам будет дано {model.total_candies} конфет, '
                                                 f'за один ход мы можем взять не более {model.max_take} конфет. '
                                                 f'Побеждает тот, кто заберет последнюю конфету. Итак, начнём!')