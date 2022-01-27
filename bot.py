import telebot
import time
import random
from decouple import config
ADMIN_ID = config('ADMIN_ID')
BOT_CREATOR_ID = config('BOT_CREATOR_ID')
BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def choose_random(number):
    my_list = open("students_list.txt", "r")
    students_list = my_list.readlines()
    my_list.close()
    a = []
    number = int(number)
    for i in range(0,number):
        choosen_one = random.randint(0,len(students_list)-1)
        a.append(students_list[choosen_one])
        del students_list[choosen_one]
    new_file = open("students_list.txt", "w+")
    for line in students_list:
        new_file.write(line)
    new_file.close()
    return(a)

@bot.message_handler(commands=['reset'])
def reset(message):
    if str(message.from_user.id) == BOT_CREATOR_ID or str(message.from_user.id) == ADMIN_ID:
        my_list = open("backup.txt", "r")
        students_list = my_list.readlines()
        my_list.close()
        new_file = open("students_list.txt", "w+")
        for line in students_list:
            new_file.write(line)
        new_file.close()
        bot.reply_to(message, 'ﻝیﺲﺗ ﺭیﺲﺗ ﺵﺩ.')
    else:
        bot.reply_to(message,"ﺶﻣﺍ ﻕﺍﺩﺭ ﺐﻫ ﺎﻨﺟﺎﻣ ﺍیﻥ ﺪﺴﺗﻭﺭ ﻥیﺲﺗیﺩ.")

@bot.message_handler(commands=['get1'])
def get_a_person(message):
    if str(message.from_user.id) == BOT_CREATOR_ID or str(message.from_user.id) ==ADMIN_ID:
        a = choose_random(1)
        for student in a:
            bot.send_message(chat_id = BOT_CREATOR_ID,text=f"{student}")
            bot.send_message(chat_id = ADMIN_ID,text=f"{student}")
    else:
        bot.reply_to(message,"ﺶﻣﺍ ﻕﺍﺩﺭ ﺐﻫ ﺎﻨﺟﺎﻣ ﺍیﻥ ﺪﺴﺗﻭﺭ ﻥیﺲﺗیﺩ.")


@bot.message_handler(commands=['get2'])
def get_two_person(message):
    if str(message.from_user.id) == BOT_CREATOR_ID or str(message.from_user.id) == ADMIN_ID:
        a = choose_random(2)
        for student in a:
            bot.send_message(chat_id = BOT_CREATOR_ID,text=f"{student}")
            bot.send_message(chat_id = ADMIN_ID,text=f"{student}")
    else:
        bot.reply_to(message,"ﺶﻣﺍ ﻕﺍﺩﺭ ﺐﻫ ﺎﻨﺟﺎﻣ ﺍیﻥ ﺪﺴﺗﻭﺭ ﻥیﺲﺗیﺩ.")

@bot.message_handler(commands=['add_to_list'])
def add_to_list(message):
    if str(message.from_user.id) == BOT_CREATOR_ID or str(message.from_user.id) == ADMIN_ID:
        msg = bot.reply_to(message, 'ﻥﺎﻣ ﻑﺭﺩی کﻩ ﻡیﺥﻭﺎﻫیﺩ ﺐﻫ ﻝیﺲﺗ ﺎﺿﺎﻔﻫ ﺵﻭﺩ ﺭﻭ ﺎﻋﻼﻣ کﻥیﺩ.')
        bot.register_next_step_handler(msg, choosing_one)
    else:
        bot.reply_to(message,"ﺶﻣﺍ ﻕﺍﺩﺭ ﺐﻫ ﺎﻨﺟﺎﻣ ﺍیﻥ ﺪﺴﺗﻭﺭ ﻥیﺲﺗیﺩ.")


def choosing_one(message):
    if message.text != None:
        my_list = open("students_list.txt", "r")
        students_list = my_list.readlines()
        my_list.close()
        students_list.append("\n"+message.text)                                                                                                                    
        new_file = open("students_list.txt", "w+")
        for line in students_list:
            new_file.write(line)
      
@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(chat_id = BOT_CREATOR_ID,text=f"salam + {str(message.from_user.id)}")
    bot.send_message(chat_id = ADMIN_ID, text=f"salam + {str(message.from_user.id)}")


while True:
    try:
        bot.polling()
    except:
        time.sleep(15)