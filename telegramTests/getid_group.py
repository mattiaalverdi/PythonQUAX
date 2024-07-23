from telegram.ext import Updater, MessageHandler, Filters

def get_chat_id(update, context):
    chat_id = update.message.chat_id
    print(f"Chat ID: {chat_id}")

if __name__ == "__main__":
    # Token del bot Telegram
    bot_token = "7336207064:AAEBqyI5fLsx6QH_slMXsFRp3o80FKRlbbs"

    # Inizializza l'updater
    updater = Updater(token=bot_token, use_context=True)

    # Ottieni dispatcher per registrare i gestori
    dp = updater.dispatcher

    # Aggiungi gestore di messaggi per ottenere l'ID della chat
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_chat_id))

    # Avvia il bot
    updater.start_polling()

    # Mantieni il bot in esecuzione fino a quando non viene interrotto
    updater.idle()
