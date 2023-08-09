import hashlib
from aiogram import Router, F, html
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

router = Router()

@router.inline_query()
async def test_query(inline_query: InlineQuery):
    content = inline_query.query
    result_id = hashlib.sha1(content.encode()).hexdigest()
    result = InlineQueryResultArticle(
            id=result_id,
            title='That\'s your result!',
            description='It is a description',
            input_message_content=InputTextMessageContent(
                message_text=f'{html.bold(html.italic(inline_query.query))}',
                parse_mode='HTML'
                    )
            )
    await inline_query.answer([result])
