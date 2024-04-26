import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import other_handlers, user_handlers


# Функция конфигурирования и запуска бота
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())