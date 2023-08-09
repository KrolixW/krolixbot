from aiogram import Router, F, html
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.reply(f'''<b>Hello, {message.from_user.full_name}!</b>
This is my demo bot to show what I can do.
Please prceed.''',parse_mode='HTML')

@router.message(Command('repeat'))
async def repeat_command(message: Message, command: CommandObject):
    await message.reply(f'You said: {html.italic(command.args)}',
                        parse_mode='HTML')
