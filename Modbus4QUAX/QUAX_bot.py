from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
import nest_asyncio
import asyncio
from telegram.error import RetryAfter

#----------------------------------------------------------------------------------------------------------------
# GLOBAL DEFINITIONS

# Sostituisci 'YOUR_BOT_TOKEN' con il token del tuo bot
TOKEN = '7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs'

# Chat ID dove inviare i messaggi
CHAT_ID = '-1002249313421'

# Inizializza il bot
bot = Bot(token=TOKEN)

#----------------------------------------------------------------------------------------------------------------
# FUNCTIONS

# Configura il logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Funzione per gestire il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")

async def send_message_async(message: str) -> None:
    try:
        # Invia il messaggio al gruppo
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except RetryAfter as e:
        # Attende il tempo specificato prima di riprovare
        wait_time = e.retry_after
        print(f"Flood control exceeded. Retrying in {wait_time} seconds...")
        await asyncio.sleep(wait_time)
        # Riprovare l'invio del messaggio
        await send_message_async(message)

def send_message_sync(message: str) -> None:
    # Crea un nuovo loop degli eventi se necessario
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    try:
        # Esegui l'invio del messaggio
        loop.run_until_complete(send_message_async(message))
    finally:
        # Non chiudere il loop se è in uso da altre funzioni asincrone
        if loop.is_running():
            loop.stop()

def QUAX_bot() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler(command="start", callback=start))
    
    # Avvia il bot
    application.run_polling()

# Applica nest_asyncio per consentire l'annidamento del loop degli eventi
nest_asyncio.apply()

#----------------------------------------------------------------------------------------------------------------
# TEST of the bot functionality
if __name__ == "__main__":    
    # Invia un messaggio di test
    send_message_sync("Test message from bots: 🟢 🔴 🟡\n Here is a message with emojis on different lines:\n🟢\n🔴\n🟡")
    
    # Avvia il bot
    QUAX_bot()
