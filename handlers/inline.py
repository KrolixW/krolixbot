import hashlib
from aiogram.enums import parse_mode
import requests
from aiogram import Router, F, html
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

router = Router()


@router.inline_query(F.query.startswith('lg'))
async def ler_me_google(inline_query: InlineQuery):
    content = inline_query.id
    result_id = hashlib.sha1(content.encode()).hexdigest()
    if inline_query.query:
        args = inline_query.query.split(';')
        if len(args) >= 2:
            link = f'https://letmegooglethat.com/?q={args[1].replace(" ","+")}'
            message = f'{args[2]}' if len(args) >= 3 else ''
            link_text = f'{html.link(args[3],link)}' if len(args) >= 4 else link
            desc = args[3] if len(args) >= 4 else link
            result = InlineQueryResultArticle(
                id=result_id,
                title=f'Let me google that for you',
                description=f'{message} {desc}',
                input_message_content=InputTextMessageContent(
                    message_text=f'{message} {link_text}',
                    parse_mode='HTML',
                    disable_web_page_preview=True
                        )
                )
            await inline_query.answer([result])

@router.inline_query(F.query == 'test')
async def test_query(inline_query: InlineQuery):
    content = inline_query.id
    result_id = hashlib.sha1(content.encode()).hexdigest()
    results = [InlineQueryResultArticle(
            id=result_id+f'{i}',
            title=f'Test №{i}',
            description=f'This is a test №{i}',
            input_message_content=InputTextMessageContent(
                message_text=f'{i}',
                parse_mode='HTML'
                    )
            ) for i in range(1,11)]
    await inline_query.answer(results)

@router.inline_query(F.query == 'quote')
async def quote_query(inline_query: InlineQuery, qapi_url):
    response = requests.get(f'{qapi_url}')
    quotes = response.json()['payload']
    offset = int(inline_query.offset) if inline_query.offset else 1
    results = []
    for i in range((offset-1)*10, offset*10):
        article = InlineQueryResultArticle(
                id = f'quote_{i}',
                title = quotes[i]['quote_by']['name'],
                description = quotes[i]['quote'],
                input_message_content=InputTextMessageContent(
                    message_text=f'{html.italic(quotes[i]["quote"])}\n\t\t {quotes[i]["quote_by"]["name"]}',
                    parse_mode='HTML')
                )
        results.append(article)
    await inline_query.answer(results,next_offset=str(offset+1))
