import telebot
from random import randint

bot = telebot.TeleBot('5409368278:AAF0lgfN8Kjo8kRLyOXA2GYXUXzSXc_qsQU')

@bot.message_handler(commands=['start'])

def get_text_messages(message):
    x = randint(1, 4)
    if message.text == "/start":
        bot.send_message(message.chat.id, """Привет! Отвечу на любой вопрос!
Вопрос должен подразумевать ответ 'Да' либо 'Нет'.
Не забудь подписаться на мой канал: https://t.me/ywchanel""")

@bot.message_handler(content_types=['text'])
def start_message(message):
    x = randint(0, 4)
    ans1 = open('yes.ogg', 'rb')
    ans2 = open('no.ogg', 'rb')
    ans3 = open('haha.ogg', 'rb')
    ans4 = open('din.ogg', 'rb')
    ans5 = open('oaoaoa.ogg', 'rb')
    ans6 = open('nikalol.ogg', 'rb')
    ques = [ans1, ans2, ans3, ans4, ans5, ans6]
    if "?" in message.text:
        bot.send_voice(message.chat.id, ques[x])


bot.polling(none_stop=True, interval=0)