import time
import telebot
import threading

TELEGRAM_TOKEN = '6125238549:AAHv5BKCAd4XBOFxQrnBPzILTHtpV-eM-bM'
MI_CHAT_ID = 1639893728
CHAT_ID_GROUP = -972894475

# Creamoe el objeto bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# commands=['command name'] recibe una lista de comandos que ejecutan la función. Esta lista no tiene porque ser uno solo, pueden ser varios comandos que ejecuten una misma función.
@bot.message_handler(commands=['start'])
def cmd_start(message):
    # Citamos el mensaje que envío el usuario y le respondemos con nuestro mensaje
    bot.reply_to(message, 'Hola qué tal?')
    # Obtener el chatid de quien envía el mensaje (es decir, el usuario)
    print(message.chat.id)


# content_type puede ser texto, documentos, imágenes, etc. Todos los tipos de contenido se encuentran explicados en la documentación oficical.
@bot.message_handler(content_types=['text', 'photo'])
def bot_send_message(message):
    if message.text and message.text.startswith('/'):
        # Para enviar un mensaje debemos pasarle como parámetro al método send_message el chatid que recibimos del usuario, y luego el texto que queremos enviar
        bot.send_message(message.chat.id, 'Comando no disponible')
    else:
        # Modificar los estados del bot. Por ejemplo: que aparezca que el bot está escribiendo o en línea, etc. Por defecto dura 5 segundos como mínimo
        bot.send_chat_action(message.chat.id, 'typing')

        sended_message = bot.send_message(message.chat.id, 'Hola...')
        time.sleep(1)
        # Editar mensaje enviado. Le pasamos el nuevo mensaje, el id del chat en el que queremos enviar el mensaje y luego el id del mensaje que queremos editar
        bot.edit_message_text('Mensaje editado', message.chat.id, sended_message.message_id)
        # Borrar mensaje
        time.sleep(1)
        bot.delete_message(message.chat.id, sended_message.message_id)
        # Eliminar el mensaje del usuario. Necesitamos el id del chat y luego el id del mensaje a eliminar, que en este caso es el id del mensaje que envío el usuario
        time.sleep(1)
        # bot.delete_message(message.chat.id, message.message_id)
        # Enviar imágenes
        with open('photo.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, 'caption of photo')
        # Enviar documentos
        with open('document.pdf', 'rb') as doc:
            bot.send_photo(message.chat.id, doc, 'caption of document')




@bot.message_handler(commands=['html', 'markdown'])
def cmd_send_html(message):
    html = '''
    <b>Texto en negrita</b> 
    <i>Texto en itálica</i>
    <span class="tg-spoiler">Spoiler text</span>
    <a href"https://www.google.com">Link</a>
    '''

    markdown = '''
    # Título
    ## Subtítulo
    ||spoiler||
    **texto en negrita**
    *Itálica*
    '''

    bot.send_message(message.chat.id, html, parse_mode='html', disable_web_page_preview=True)
    bot.send_message(message.chat.id, markdown, parse_mode='markdownV2', disable_web_page_preview=True)





if __name__ == '__main__':
    print('Iniciando el bot...')
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Descripción del comando start'),
        telebot.types.BotCommand('/text', 'Descripción del comando text'),
        telebot.types.BotCommand('/hello', 'Descripción del comando hello'),
        telebot.types.BotCommand('/to_html', 'Descripción del comando to_html')
    ])
    bot.send_message(CHAT_ID_GROUP, 'Hola este es el grupo')
    bot.infinity_polling()
    print('Fin')


