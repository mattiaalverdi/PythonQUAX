from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, Updater
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Sostituisci 'YOUR_BOT_TOKEN' con il token del tuo bot
TOKEN = '7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs'

# Chat ID dove inviare i messaggi
CHAT_ID = 'YOUR_CHAT_ID'

# Inizializza il bot
bot = Bot(token=TOKEN)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")
    
async def PressureUpdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")    

# Funzione per inviare un messaggio in chat
async def send_text_message(text: str) -> None:
    bot.send_message(chat_id=CHAT_ID, text=text)

def QUAX_bot() -> None:
    application = Application.builder().token("7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs").build()

    application.add_handler(CommandHandler(command="start", callback=start))

    application.run_polling()



#----------------------------------------------------------------------------------------------------------------
# TEST of the bot functionality
if __name__ == "__main__":    
    QUAX_bot()