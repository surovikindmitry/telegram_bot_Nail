from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
#пока не нужен без стейтов


dp = Dispatcher(bot, storage=storage)
#самый главный обработчик апдейтов, откуда они попадают в хендлер, где настраивается логика ответов
#dispatcher дает доступ к следующим функциям dp.loop dp.bot dp.storage


#Отправка сообщения. Для остальных видов выбирать соответствующее значение
#bot.send_message()
#этот метод асинхронный, в данной функции работать не будет

#для запуска асинхронных функций использовать
#dp.loop.run_until_complete(bot.send_message)