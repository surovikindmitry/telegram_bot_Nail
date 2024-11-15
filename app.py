from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)

#при запуске файла app.py выполняются следующие команды
if __name__ == '__main__':
    from aiogram import executor
#необходимо для опроса состояния (get updates) на сервере,
    from handlers import dp
#все что прошло обработку в других функциях
#запуск get updates на сервере
    executor.start_polling(dp, on_startup=on_startup)
#on_startup необходим для регистрации функций, фильтров и прочего. прописано выше