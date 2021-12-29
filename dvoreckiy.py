#from abc import update_abstractmethods
from datetime import datetime

import telebot
TOKEN = '5031663337:AAFZe9Ve8CTEvtnDtAuWrubToAZbFh8zGdY'

#variables for alarm
now = datetime.now()
time = now.strftime("%H:%M")
day=datetime.today().isoweekday()


#TOKEN intializaton
bot = telebot.TeleBot (TOKEN)

# common Menu Inline keyboard(buttons)
start_markup = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('Будильник', callback_data='1')
btn2 = telebot.types.InlineKeyboardButton('Бугхалтер',url = "https://t.me/FinBuhgalter_bot")
btn3 = telebot.types.InlineKeyboardButton('Развлечения', callback_data='3')
btn4 = telebot.types.InlineKeyboardButton('Помощь', callback_data='4')
btn5 = telebot.types.InlineKeyboardButton('Банкоматы', callback_data=5)
btn6 = telebot.types.InlineKeyboardButton('Цены столовой', callback_data='6')
btn7 = telebot.types.InlineKeyboardButton('Цены в буфете', callback_data='7')
start_markup.add(btn1,btn2,btn3, btn4, btn5, btn6, btn7)

#KTL/DL keyboard
tur = telebot.types.InlineKeyboardMarkup()
ktl = telebot.types.InlineKeyboardButton('KTL', callback_data='8')
dl = telebot.types.InlineKeyboardButton('DL', callback_data='9')
tur.add(ktl,dl)

#"start" command reaction/handler
@bot.message_handler(commands=["start"])
def hi(message):
    #bot.send_sticker(message.chat.id, open('/Users/Adish/PycharmProjects/pythonProject/Welcome.tgs', 'rb'))
    bot.send_message(message.chat.id,'Привет, '+message.from_user.first_name+'! Я Dvoreckiy, портативный ассистент во время твоего обучения. Для того чтобы подробно ознакомится с моими возможностями выбери одну из функций.', reply_markup = start_markup)

# "alarm" command reaction/handler
@bot.message_handler(commands=["alarm"])
def alarm(message):
    #messages for turkish group confirmation
    bot.send_message(message.chat.id,"Я твой будильник, который заработал после нажантия на кнопку \"Будильник\".\nЯ буду по умолчанию предупреждать тебя за 10 минут до предстоящей пары.")
    bot.send_message(message.chat.id,"Но для начала мне нужно знать в какой ты группе?",reply_markup=tur)
    #common alarm call
    if day == 1 and time == "16:02":
        bot.send_message(message.chat.id, "У тебя скоро Calculus1-online.\nhttps://zoom.us/j/6511666327?pwd=a2xyazlKRFFhamNQcnVCL1I0cE9kdz09")
    elif day == 1 and time == "12:50":
        bot.send_message(message.chat.id, "У тебя скоро физическая культура.Иди в спортзал")
    elif day == 2 and time == "08:50":
        bot.send_message(message.chat.id, "У тебя скоро экология в В113.")
    elif day == 2 and time == "13:30":
        bot.send_message(message.chat.id, "У тебя скоро Algebra & Geometry в В205.")
    elif day == 2 and time == "16:20":
        bot.send_message(message.chat.id, "У тебя скоро Engineering Computer Graphics в Big Lab.")
    elif day == 3 and time == "08:50":
        bot.send_message(message.chat.id, "У тебя скоро Programming Language 1 в Big Lab.")
    elif day == 3 and time == "12:10":
        bot.send_message(message.chat.id, "У тебя скоро Русский язык.")
    elif day == 3 and time == "14:40":
        bot.send_message(message.chat.id, "У тебя скоро Programming Language 1 Practice в Big Lab.")
    elif day == 4 and time == "08:50":
        bot.send_message(message.chat.id, "У тебя скоро Physics 1-online.")
    elif day == 5 and time == "08:50":
        bot.send_message(message.chat.id,
                         "У тебя скоро Calculus1-online.\nhttps://zoom.us/j/6511666327?pwd=a2xyazlKRFFhamNQcnVCL1I0cE9kdz09.")

    # for free hours
    elif day == 2 and time == "10:30":
        bot.send_message(message.chat.id,
                         'Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/')
    elif day == 3 and time == "10:30":
        bot.send_message(message.chat.id,
                         'Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/')
    elif day == 4 and time == "12:10":
        bot.send_message(message.chat.id,
                         'Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/')
    elif day == 5 and time == "11:20":
        bot.send_message(message.chat.id,
                         'Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/')


# "fin" command reaction/handler
@bot.message_handler(commands=["fin"])
def fin(message):
    bot.send_message(message.chat.id,"https://t.me/FinBuhgalter_bot")

# "ent" command reaction/handler
@bot.message_handler(commands=["ent"])
def ent(message):
    bot.send_message(message.chat.id,'Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/')

# "help" command reaction/handler
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "У тебя возникли вопросы?\nТогда напиши команде разработчиков бота Dvoreckiy, чтобы получить ответы от создателей твоего помошника.\n https://t.me/+PmmjSc0X0HwxM2Yy\n Пожалуйста, перейди по ссылке или просканируй QR-код ниже.")
    #bot.send_photo(message.chat.id, photo)
    #bot.send_sticker(message.chat.id, s_help)

# "atms" command reaction/handler
@bot.message_handler(commands=["atms"])
def atms(message):
    bot.send_message(message.chat.id, "Это список банкоматов в радиусе 1.5 км.\n\n DemirBank\n11:30-03:00\nhttps://go.2gis.com/qw53t\n\nDemirBank\n08:00-23:00\nhttps://go.2gis.com/nwyg1\n\nDemirBank\n08:00-21:00\nhttps://go.2gis.com/qgbq50\n\nАйыл Банк\n8:00-18:00\nhttps://go.2gis.com/9ewb4p\n\nOptima Bank\n27/7\nhttps://go.2gis.com/c4hxr\n\nКеремет Банк\n09:00-19:00\nhttps://go.2gis.com/i2yd44\n\nDemiBank\n07:00-24:00\nhttps://go.2gis.com/b89p7\n\nKICB\n24/4\nhttps://go.2gis.com/kl9lk\n\nKICB\n09:00-19:00\nhttps://go.2gis.com/3ik3d5\n\nКЫРГЫЗСТАН\n24/7\nhttps://go.2gis.com/plkzm\n\nРСК\n08:00-24:00\nhttps://go.2gis.com/v3x3d\n\n")

# "price_l_stolov" command reaction/handler
@bot.message_handler(commands=["price_l_stolov"])
def price_l_stolov(message):
    bot.send_message(message.chat.id, "Плов 100\nКомбо(Рис -Пюре 40+ подлив) 100\nМясной подлив 50\nЧечевичный суп 60\nСосиска 30\nКотлета 30\nКурица 50\nДесерты 50-65\nСалаты 50\nЙогурт 50\nБлинчики 30")

# "atms" command reaction/handler
@bot.message_handler(commands=["price_l_kantin"])
def price_l_kantin(message):
    bot.send_message(message.chat.id, "Самсы с курицей 45\nСамсы с сыром 30\nСамсы с картошкой 30\nСамсы с мясом 50\nПицца 80\nСимит 15\nКруассан 40\nПиде 50\nДесерты 65\nТост с колбасой 80\nСэндвич 70\nБорек с сыром 40\nСимит 25\nКорзинка с овощами 11\nКорзинка с сыром 10\nКорзинка с оливками 15\nТост с сыром 50\nПиде с сыром 40\nЧизкейк 65\nБрауни 50\nКоднитерские пироженые 65\nЧалап  30")

# inline common keyboard handler
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data=="1":
            bot.send_message(call.message.chat.id, "Я твой будильник, который заработал после нажантия на кнопку \"Будильник\".\nЯ буду по умолчанию предупреждать тебя за 10 минут до предстоящей пары.")
            bot.send_message(call.message.chat.id, "Но для начала мне нужно знать в какой ты группе?",reply_markup=tur)
        elif call.data == "3":
            bot.send_message(call.message.chat.id,"Если у тебя окно или тебе нечем заняться, пройди по этим ссылкам , чтобы немного побаловать  свой мозг!.\nhttps://brainapps.ru/\nhttps://www.udemy.com/\nhttps://darebee.com/\nhttps://iamthecu.be/\nhttps://paperplanes.world/\nhttp://stars.chromeexperiments.com/\nhttps://virtualpiano.net/")
        elif call.data == "4":
            bot.send_message(call.message.chat.id, "У тебя возникли вопросы?\nТогда напиши команде разработчиков бота Dvoreckiy, чтобы получить ответы от создателей твоего помошника.\n https://t.me/+PmmjSc0X0HwxM2Yy\n Пожалуйста, перейди по ссылке или просканируй QR-код ниже.")
        elif call.data=="5":
            bot.send_message(call.message.chat.id, "Это список банкоматов в радиусе 1.5 км.\n\n DemirBank\n11:30-03:00\nhttps://go.2gis.com/qw53t\n\nDemirBank\n08:00-23:00\nhttps://go.2gis.com/nwyg1\n\nDemirBank\n08:00-21:00\nhttps://go.2gis.com/qgbq50\n\nАйыл Банк\n8:00-18:00\nhttps://go.2gis.com/9ewb4p\n\nOptima Bank\n27/7\nhttps://go.2gis.com/c4hxr\n\nКеремет Банк\n09:00-19:00\nhttps://go.2gis.com/i2yd44\n\nDemiBank\n07:00-24:00\nhttps://go.2gis.com/b89p7\n\nKICB\n24/4\nhttps://go.2gis.com/kl9lk\n\nKICB\n09:00-19:00\nhttps://go.2gis.com/3ik3d5\n\nКЫРГЫЗСТАН\n24/7\nhttps://go.2gis.com/plkzm\n\nРСК\n08:00-24:00\nhttps://go.2gis.com/v3x3d")
        elif call.data=="6":
            bot.send_message(call.message.chat.id, "Плов 100\nКомбо(Рис -Пюре 40+ подлив) 100\nМясной подлив 50\nЧечевичный суп 60\nСосиска 30\nКотлета 30\nКурица 50\nДесерты 50-65\nСалаты 50\nЙогурт 50\nБлинчики 30")
        elif call.data=="7":
            bot.send_message(call.message.chat.id, "Самсы с курицей 45\nСамсы с сыром 30\nСамсы с картошкой 30\nСамсы с мясом 50\nПицца 80\nСимит 15\nКруассан 40\nПиде 50\nДесерты 65\nТост с колбасой 80\nСэндвич 70\nБорек с сыром 40\nСимит 25\nКорзинка с овощами 11\nКорзинка с сыром 10\nКорзинка с оливками 15\nТост с сыром 50\nПиде с сыром 40\nЧизкейк 65\nБрауни 50\nКоднитерские пироженые 65\nЧалап  30")

    ## KTL/DL inline keyboard command reaction/handler
        elif call.data=="8":
            bot.send_message(call.message.chat.id,"Спасибо за ответ.")
            if day==2 and time=="11:20":
                bot.send_message(call.message.chat.id,"У тебя скоро турецкий в В201.")
            elif day==4 and time=="13:50":
                bot.send_message(call.message.chat.id,"У тебя скоро турецкий в В202.")
        if call.data=="9":
            bot.send_message(call.message.chat.id, "Спасибо за ответ.")
            if day==1 and time=="11:20":
                bot.send_message(call.message.chat.id,"У тебя скоро турецкий в В блоке.")
    except  Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
