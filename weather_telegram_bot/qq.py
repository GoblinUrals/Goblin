import os
import telebot
import logging
from config import *
from flask import Flask, request

bot = telebot.Telebot(tg_bot_token)
server = Flask(__name__)
logger = telebot.logger
logger.setlevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.username
    bot.reply_to(message, f"Hello, {username}!")

@server.route(f"/{tg_bot_token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webnook()
    bot.set_webnook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


