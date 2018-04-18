from telegram.ext import Updater, MessageHandler, Filters
import re

token = "TOKEN"

updater = Updater(token=token)
dispatcher = updater.dispatcher
qingzhen_re = re.compile("[\u0600-\u06ff\u0750-\u077f\ufd50-\ufdcf\ufdf0-\ufdff\ufe70-\ufeff]")


def is_qingzhen(name):
    if (qingzhen_re.search(name)):
        print(qingzhen_re.search(name))
        return True
    else:
        return False


def check_new_user(bot, update):
    if update.message.new_chat_members != []:
        print(update.message.new_chat_members[0])
        name = update.message.new_chat_members[0].first_name
        if is_qingzhen(name):
            bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.new_chat_members[0].id)


dispatcher.add_handler(MessageHandler([Filters.status_update], check_new_user))
updater.start_polling()
updater.idle()
