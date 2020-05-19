from config import TOKEN
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(CommandHandler('prueba', bot.prueba))

    # El orden importa
    dispatcher.add_handler(CallbackQueryHandler(bot.menu_main, pattern='main'))
    dispatcher.add_handler(CallbackQueryHandler(bot.ver_todas,
                                                pattern='all'))
    dispatcher.add_handler(CallbackQueryHandler(bot.ver_constelacion, pattern='constellation'))
    dispatcher.add_handler(CallbackQueryHandler(bot.ver_estrellas, pattern='stars'))
    dispatcher.add_handler(CallbackQueryHandler(bot.cargar_constelacion))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
