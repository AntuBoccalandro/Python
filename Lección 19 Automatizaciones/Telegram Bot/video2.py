import telebot

TELEGRAM_TOKEN = '6125238549:AAHv5BKCAd4XBOFxQrnBPzILTHtpV-eM-bM'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

data = {}

@bot.message_handler(commands=['register'])
def register(message):
    markup = telebot.types.ForceReply()
    msg = bot.send_message(message.chat.id, 'Ingrese su nombre: ', reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_edad)


def preguntar_edad(message):
    markup = telebot.types.ForceReply()
    msg = bot.send_message(message.chat.id, 'Ingrese su edad: ', reply_markup=markup)
    data[message.chat.id] = {}
    data[message.chat.id]['nombre'] = message.text
    bot.register_next_step_handler(msg, preguntar_genero)

def preguntar_genero(message):
    if not message.text.isdigit():
        markup = telebot.types.ForceReply()
        msg = bot.send_message(message.chat.id, 'Ingrese su edad: ', reply_markup=markup)
        bot.register_next_step_handler(msg, preguntar_edad)
    else:
        data[message.chat.id]['edad'] = message.text
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, 
                                                   input_field_placeholder='Elige una opción',
                                                   resize_keyboard=True
                                                    )
        markup.add('Hombre', 'Mujer')
        msg = bot.send_message(message.chat.id, 'Elige tu género: ', reply_markup=markup)
        bot.register_next_step_handler(msg, registrar_datos)


def registrar_datos(message):
    if message.text != 'Hombre' and message.text != 'Mujer':
        markup = telebot.types.ForceReply()
        msg = bot.send_message(message.chat.id, 'Género no válido ', reply_markup=markup)
        bot.register_next_step_handler(msg, preguntar_genero)
    else:
        data[message.chat.id]['genero'] = message.text
        print(data)
        


if __name__ == '__main__':
    bot.infinity_polling()

