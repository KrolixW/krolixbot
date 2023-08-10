import os
import logging
import asyncio
from aiogram import Dispatcher, Bot
from handlers import commands, inline

async def main():
    # Get API Token
    API_TOKEN = str(os.getenv('KROLIX_BOT_TOKEN'))

    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Include routers
    dp.include_routers(commands.router,
                       inline.router)

    # Droup updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

