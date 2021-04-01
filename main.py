from bot import server, bot

import os


def main():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']='linker_sender/linkersenderv2-f2b5ee0d0663.json'
    bot.remove_webhook()
    bot.polling(True)
    #server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


if __name__ == '__main__':
    main()
