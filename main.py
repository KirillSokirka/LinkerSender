import config

from bot import bot


def main():
    bot.delete_webhook()
    bot.polling(True)

if __name__ == '__main__':
    main()
