import telebot
import time
import random

bot = telebot.TeleBot("1668849232:AAGgE5yCtFP2PwAHa9Y7MqcIJzmrJYHuwIQ")

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
    if str(message.from_user.id) == "210500717":
        my_list = open("backup.txt", "r")
        students_list = my_list.readlines()
        my_list.close()
        new_file = open("students_list.txt", "w+")
        for line in students_list:
            new_file.write(line)
        new_file.close()
        bot.reply_to(message, 'لیست ریست شد.')
    else:
        bot.reply_to(message,"شما قادر به انجام این دستور نیستید.")


@bot.message_handler(commands=['get1'])
def get_a_person(message):
    if str(message.from_user.id) == "210500717":
        a = choose_random(1)
        for student in a:
            bot.send_message(chat_id = "210500717",text=f"{student}")
            bot.send_message(chat_id = "-599363155",text=f"{student}")
            # bot.send_message(chat_id = "210500717",text=f"{studet}")
        else:
            bot.reply_to(message,"شما قادر به انجام این دستور نیستید.")


@bot.message_handler(commands=['get2'])
def get_two_person(message):
    if str(message.from_user.id) == "210500717":
        a = choose_random(2)
        for student in a:
            bot.send_message(chat_id = "210500717",text=f"{student}")
            bot.send_message(chat_id = "-599363155",text=f"{student}")
            # bot.send_message(chat_id = "210500717",text=f"{studet}")
    else:
        bot.reply_to(message,"شما قادر به انجام این دستور نیستید.")

@bot.message_handler(commands=['add_to_list'])
def add_to_list(message):
    if str(message.from_user.id) == "210500717":
        msg = bot.reply_to(message, 'نام فردی که میخواهید به لیست اضافه شود رو اعلام کنید.', reply_markup=keyboard)
        bot.register_next_step_handler(msg, choosing_one)
    else:
        bot.reply_to(message,"شما قادر به انجام این دستور نیستید.")

def choosing_one(message):
    if message.text != None:
        my_list = open("students_list.txt", "r")
        students_list = my_list.readlines()
        my_list.close()
        students_list.append("\n"+message.text)
        new_file = open("students_list.txt", "w+")
        for line in students_list:
            new_file.write(line)
        new_file.close()
        bot.reply_to(message , "فرد مورد نظر به لیست افراد اضافه شد.")

message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message,"Welcome")
    # if str(message.from_user.id) == "210500717":
    # bot.reply_to(message, 'به بات خوش آمدید. این بات هر جمعه صبح به شما اسامی دو نفر را خواهد داد.')
    # students_list = backup.split("\n")
    # for i in range(0,42):
    #     a = []
    #     for i in range(0,2):
    #         choosen_one = random.randint(0,len(students_list)-1)
    #         bot.send_message(chat_id= message.chat.id , text= students_list[choosen_one])
    #         a.append(students_list[choosen_one])
    #         del students_list[choosen_one]
    #     # for save a list from who choosed before
    #     done_list = open("student_list.txt", "a+")
    #     done_list.write(a)

while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
