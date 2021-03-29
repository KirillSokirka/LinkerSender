import config

import telebot
from telebot import types

bot = telebot.TeleBot(config.Token)

from flask import Flask, request
server = Flask(__name__)

@server.route('/' + config.Token, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!",200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://linkersender.herokuapp.com/' + config.Token)
    return "!", 200

@bot.message_handler(commands = ['start'])
def say_hello(message):
    bot.send_message(message.chat.id,
                     'Привіт, я <b>LinkerSender</b>!'+
                     'Я створений, щоб вибирати всі посилання з твої пошти ' +
                     'та надсилати їх тобі у Telegram', parse_mode='html')
    animation = open(config.HelloSticker, 'rb')
    bot.send_animation(message.chat.id, animation)

@bot.message_handler(commands=['enter_channel'])
def send_link(message):
    bot.send_message(message.chat.id, 'Посилання на канал - ' + config.LinkToChannel)

@bot.message_handler(content_types=['text'])
def post_to_channel(message):
    bot.send_message(config.ChannelName, message)


