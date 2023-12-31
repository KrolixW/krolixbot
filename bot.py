import logging
from os import getenv

from aiohttp import web

from aiogram import Dispatcher, Bot
from handlers import commands, inline
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Get API Token
API_TOKEN = str(getenv('KROLIX_BOT_TOKEN'))

# Webhook configs
WEB_SERVER_HOST = getenv('WEB_SERVER_HOST')

WEB_SERVER_PORT = getenv('WEB_SERVER_PORT')

WEBHOOK_PATH = getenv('WEBHOOK_PATH')
BASE_WEBHOOK_URL = getenv('BASE_WEBHOOK_URL')
WEBHOOK_SECRET = getenv('WEBHOOK_SECRET')
QAPI_URL = getenv('QAPI_URL')

async def on_startup(bot: Bot):
    await bot.set_webhook(f'{BASE_WEBHOOK_URL}{WEBHOOK_PATH}',secret_token=WEBHOOK_SECRET)

def main():


    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Include routers
    dp.include_routers(commands.router,
                       inline.router)
    dp.startup.register(on_startup)

    app = web.Application()
    webhook_request_handler = SimpleRequestHandler(dispatcher=dp,bot=bot,secret_token=WEBHOOK_SECRET, qapi_url = QAPI_URL)
    webhook_request_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
if __name__ == '__main__':
    main()

