import asyncio
from aiogram import Bot, Dispatcher
import config
from routers import user, admin


async def main():
    bot = Bot(config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(user.router, admin.router)
    await dp.start_polling(bot)


asyncio.run(main())
