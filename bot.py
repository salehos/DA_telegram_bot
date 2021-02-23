import telebot
import time
import random

backup = """mohammad-azari
mohammad mahdi-danesh pazhoh
amir mohammad-gholiha
kasra-damavandi asl
mohammad amin-motahari nia
alireza-rahmani
mohammad hanif-saadaei jahromi
mohammad saleh-saeidi
mohsen-kasiri
amir hosein-asem yousefi
sina-mavali
reza-amini mojed
alireza-eilami
mohamad javad-hamzeh
parham-saremi
yasaman-samad zadeh
abolfazl-asad
danial-esfini farahani
mahsa-amani
ali-javanmard
fatemeh-khashe ei
bahar-khodabakhshian
dorna-dehghani
ahmad-zaaferani
nima-salem ahim
hosein-sobhi
majid-taher khani
mohammad matin-fotohi
amirhosein-farahani
sajjad-faghfour maghrebi
ali asghar-ghanaei
seyed mohammad sadegh-keshavarzi
mehregan-nazar mohseni facori
mohammad-shojaeian
kian-baakhtari
mohammad ali-pashanj
seyed amir pouya-moeini
ahmad-nosrat bakhsh
diba-masihi
arshia-akhavan
parham-chavoshian
maryam saadaat-razavi taaheri
karaneh-keypour
mohammad mehdi-aboutorabi
mohammad hosein-haji seyed soleyman
abdossamad-haghiri
mehdi-salmani saleh abadi
reza-erfan arabi(araei?)
fatemeh-asgari
mohammad mahdi-gheidi
amirhosein-nedaei pour asl
parsa-hoseini
amir mohammad-imani
kian-omoumi
sara-azarnoush
peyman-haji mohammad ebrahim
kamiyar-taeb
mohammad javad-alaedini
arash-chaei melat shahi
"""

bot = telebot.TeleBot("your_token")

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, 'به بات خوش آمدید. این بات هر جمعه صبح به شما اسامی دو نفر را خواهد داد.')
    students_list = backup.split("\n")
    for i in range(0,30):
        for i in range(0,2):
            choosen_one = random.randint(0,len(students_list)-1)
            bot.send_message(chat_id= message.chat.id , text= students_list[choosen_one])
            del students_list[choosen_one]
        time.sleep(10)
        # sleep for a 604800 second or a week

while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
