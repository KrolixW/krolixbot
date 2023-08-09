from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject

router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.reply(f'''Hello, {message.from_user.first_name}!
    This is my demo bot do show what I can do.
    Please prceed. <3''')
