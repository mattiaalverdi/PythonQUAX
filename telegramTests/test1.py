from telegram import Bot
from telegram.ext import Application
import asyncio
from bot import send_text_message

async def orcocan(sandocan: str):
    bot_token = '7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs'
    chat_id = '-1002249313421'
    bot = Bot(token=bot_token)

    # Chiamata alla funzione asincrona e attendi la sua completazione
    await send_text_message(bot, chat_id, sandocan)

if __name__ == '__main__':
    asyncio.run(orcocan('vara che beo'))
