import os
import logging
import asyncio
from aiogram import Dispatcher, Bot
from handlers import commands
async def main():
    API_TOKEN = str(os.getenv('KROLIX_BOT_TOKEN'))
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Setup logging
    logging.basicConfig(level=logging.INFO)

    dp.include_router(commands.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

