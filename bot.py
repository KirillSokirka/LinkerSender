import config

import telebot

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands = ['start'])
def say_hello(message):
    bot.send_message(message.chat.id,
                     'Привіт, я <b>LinkerSender</b>!'+
                     'Я створений, щоб вибирати всі посилання з твої пошти'+
                     'та надсилати їх тобі у Telegram', parse_mode='html')
    sticker = open(config.HelloSticker, 'r')
    bot.send_sticker(message.chat.id, sticker)

