import config

import telebot
from telebot import types

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands = ['start'])
def say_hello(message):
    bot.send_message(message.chat.id,
                     'Привіт, я <b>LinkerSender</b>!'+
                     'Я створений, щоб вибирати всі посилання з твої пошти ' +
                     'та надсилати їх тобі у Telegram', parse_mode='html')
    animation = open(config.HelloSticker, 'rb')
    bot.send_animation(message.chat.id, animation)

