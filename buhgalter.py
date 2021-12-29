import logging
import re
import os
import telebot
import json
import config
import cProfile
import sched, time
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from config import API_TOKEN

API_TOKEN = config.API_TOKEN
bot = telebot.TeleBot(token=API_TOKEN)

choice = {}
users_dict = {}
CATEGORIES = ['Питание', 'Трансопрт', 'Покупки', 'Прочее']
report_MODE = ['День', 'Месяц']
bot = telebot.TeleBot(API_TOKEN)

telebot.logger.setLevel(logging.INFO)

#command start that also works as a help
@bot.message_handler(commands=['start'])
def greet_command(message):      
    greet_text = """Здравствуй, дорогой пользователь! Я Buhgalter. С моей помощью, ты сможешь отслеживать свои ежедневные или недельные расходы. Вот фичи: 
    /start':Начало,
    /new  :Начать считать расходы,
    /report:Показать отчет о расходах за день/месяц,
    /clear: Очистить историю \n\n"""
    bot.reply_to(message, greet_text)
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
#to collect spendings
def Json(users_dict):
    try:
        with open('baza.json', 'w') as json_file: 
            json.dump(users_dict, json_file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('error')

def loadJson():
    global users_dict
    try:
        if not  os.stat('baza.json').st_size == 0:
            with open('baza.json') as json_file:
                baza = json.load(json_file)
            users_dict = baza
    except FileNotFoundError:
        print('error')

#report about spendings using json
@bot.message_handler(commands=['report'])

#report command
def report_command(message):
    loadJson()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 3
    for j in report_MODE:
        markup.add(j)
    msg = bot.reply_to(message, 'За какой промежуток времени, Вы хотите увидеть отчет?', reply_markup=markup)
    bot.register_next_step_handler(msg, report)

#main function
def calculate(result):
    total = {}

    for l in result:
        s = l.split(',')
        category = s[1]
        if category in total:
            total[category] = round(total[category] + float(s[2]),2)
        else:
            total[category] = float(s[2])
    total_text = ""
    for i, value in total.items():
        total_text += str(i) + str(value) + ' ' + 'coм' + "\n"
    return total_text

Date_t = '%d-%b-%Y'
Time_t = '%H:%M'
Month_t = '%b-%Y'

def report(message):
    try:
        chat_id = message.chat.id
        period = message.text

        if not period in report_MODE:
            raise Exception("Извини, я не могу дать Вам отчет за этот промежуток времени \"{}\"!".format(period))

        history = get_history(chat_id)
        if history is None:
            raise Exception("Вы еще не записывал(-а) свои траты!")
        
        total_text = ""

        if period == 'День':
            query = datetime.now().today().strftime(Date_t)
            result_main = [value for index, value in enumerate(history) if str(query) in value] 
        elif period == 'Месяц':
            query = datetime.now().today().strftime(Month_t)
            result_main = [value for index, value in enumerate(history) if str(query) in value]
        total_text = calculate(result_main)

        spending_text = ""
        if len(total_text) == 0:
            spending_text = "На данный момент у Вас не было ни одной траты {}!".format(period)
        else:
            spending_text = "Вот все Ваши траты {}: \n----------------------\n{}".format(period.lower(), total_text)
            
        bot.send_message(chat_id, spending_text)
    except Exception as e:
        bot.reply_to(message, 'Ой!Кажется вышла ошибочка ')


@bot.message_handler(commands=['new'])
def new_command(message):
    loadJson()
    chat_id = message.chat.id
    choice.pop(chat_id, None) 
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 3
    for category in CATEGORIES:
        markup.add(category)
    msg = bot.reply_to(message, 'ВЫбери категорию пожалуйста:)', reply_markup=markup)
    bot.register_next_step_handler(msg, step)

def Amount_main(amountStr):    
    if len(amountStr) > 0 and len(amountStr) <= 15:
        if amountStr.isdigit: 
               amount = round(float(amountStr),2)
               if amount > 0:
                  return str(amount)                
    return 0

def step(message):
    try:
        chat_id = message.chat.id
        category_text = message.text

        choice[chat_id] = category_text
        message = bot.send_message(chat_id, 'Сколько Вы потратили на {}? \n(Запишите только число)'.format(str(choice[chat_id])))
        bot.register_next_step_handler(message, step2)
    except Exception as e:
        bot.reply_to(message, 'Ой!Кажется вышла ошибочка')

def step2(message):
    try:
        chat_id = message.chat.id
        amount_num = Amount_main(message.text)

        dt = datetime.today().strftime(Date_t+' '+Time_t)
        dateText, categoryText, amountText = str(dt), str(choice[chat_id]), str(amount_num)
        Json(add_history(chat_id,"{},{},{}".format(dateText,categoryText,amountText)))
        bot.send_message(chat_id, 'Вы потратили {} сом для {} на {}'.format(amountText,categoryText,dateText))
       
    except Exception as e:
        bot.reply_to(message, 'Ой!Кажется вышла ошибочка')

def get_history(chat_id):
    global users_dict
    if (str(chat_id) in users_dict):
        return users_dict[str(chat_id)]
    return None

def del_history(chat_id):
    global users_dict
    if (str(chat_id) in users_dict):
        del users_dict[str(chat_id)]
    return users_dict

def add_history(chat_id, recorded):
    global users_dict
    if not (str(chat_id) in users_dict):
        users_dict[str(chat_id)] = []
        
    users_dict[str(chat_id)].append(recorded)
    return users_dict

#clear command to clear the history of spendings
@bot.message_handler(commands=['clear'])
def clear_command(message):
    global users_dict
    chat_id = message.chat.id
    loadJson()
    clear_history_text = ""
    if (str(chat_id) in users_dict):
        Json(del_history(chat_id))
        clear_history_text = "Я очистел вашу историю расходов!"
    else:
        clear_history_text = "Ваша история расходов и так пуста."
    bot.send_message(chat_id, clear_history_text)

def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
	cProfile.run('main()')
    
