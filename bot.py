import telegram
bot = telegram.Bot(token='5245503053:AAEwDY5jl_qq-TFyAXfMQGMFnQAZ82p7mc0')
#bot.send_message(text='Hi John!', chat_id='@rrrrtfde')
def send(text):
    bot.send_message(text=text,chat_id='@rrrrtfde')