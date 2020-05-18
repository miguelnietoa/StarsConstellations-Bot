from config import TOKEN
from telegram.ext import Updater, CommandHandler
import bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("prueba", bot.prueba))

    updater.start_polling()
    updater.idle()
