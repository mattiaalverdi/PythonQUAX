from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")
    
async def PressureUpdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot! How can I help you?")    

def QUAX_bot() -> None:
    application = Application.builder().token("7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs").build()

    application.add_handler(CommandHandler(command="start", callback=start))

    application.run_polling()



#----------------------------------------------------------------------------------------------------------------
# TEST of the bot functionality
if __name__ == "__main__":    
    QUAX_bot()