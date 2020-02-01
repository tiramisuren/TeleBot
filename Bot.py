# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Variable
updater = Updater(token='960120259:AAFMKnTSOt_VcZ72TTlHV0wcVFy0egHoecM', use_context=True)
dispatcher = updater.dispatcher  


# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi welcome to Zodiac Bot. This Bot will find your horoscope in conjuction to your Zodiac!")

def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please input your Birth Date in DDMM format Eg. For 31st Jan Input <3101>")

def setHoros    cope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="INPUT")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)



# Main   
start_handler = CommandHandler('start', start) 
dispatcher.add_handler(start_handler)

date_handler = CommandHandler('setDate', setDate) 
dispatcher.add_handler(date_handler)

horoscope_handler = CommandHandler('setHoroscope', setHoroscope) 
dispatcher.add_handler(horoscope_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
print("Bot is working")