# TODA función que responde a comandos en el bot
# lleva los parámetros update y context


def start(update, context):
    update.message.reply_text("Hola mundo.")


def prueba(update, context):
    chat_id = update.message.chat.id
    context.bot.send_photo(chat_id, open('output.png', 'rb'))
