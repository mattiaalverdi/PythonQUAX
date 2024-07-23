from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, Updater
import logging
from main import PressureUpdate

# Configura il logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Sostituisci 'YOUR_BOT_TOKEN' con il token del tuo bot
TOKEN = '7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs'

# Chat ID dove inviare i messaggi
CHAT_ID = '-1002249313421'

# Inizializza il bot
bot = Bot(token=TOKEN)

# Funzione per gestire il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")

# # Funzione per gestire l'aggiornamento della pressione
# async def PressureUpdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")    

def QUAX_bot() -> None:
    application = Application.builder().token("7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs").build()

    application.add_handler(CommandHandler(command="start", callback=start))
    
    application.add_handler(CommandHandler(command="bat", callback=PressureUpdate))

    application.run_polling()

async def send_text_message(bot: Bot, chat_id: int, message: str):
    await bot.send_message(chat_id=chat_id, text=message)

async def sendStringToGroup(txtSoup: str):
    # bot_token = '7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs'
    # chat_id = '-1002249313421'
    # bot = Bot(token=bot_token)

    # Chiamata alla funzione asincrona e attendi la sua completazione
    await send_text_message(bot, CHAT_ID, txtSoup)

#----------------------------------------------------------------------------------------------------------------
# TEST of the bot functionality
if __name__ == "__main__":    
    QUAX_bot()