import telebot
import time
import random

backup = """mohammad-azari
mohammad mahdi-danesh pazhoh
amir mohammad-mohammad gholiha
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
ahmad-salimi
hosein-sobhi
majid-taher khani
mohammad matin-fotohi
amirhosein-farahani
ali asghar-ghanati
seyed mohammad sadegh-keshavarzi
mehregan-nazar mohseni fakoori
mohammad-shojaeian
kian-baakhtari
mohammad ali-pashanj
seyed amir pouya-moeini
ahmad-nosrat bakhsh
diba-masihi
parham-chavoshian
mohammad javad-hezaare
kahbod-aeini
mohhammad ali-khodabandeh loo
matin-shoja
karaneh-keypour
dorsa-majdi
mohammad ali-mohammad khani
amir-nezhad malayeri
mohammad-abol nezhadian
matin-moradi
mohammad mehdi-aboutorabi
arash-tavangar
mohammad-jafari ...
mohammad-cheraghi
mohammad hosein-haji seyed soleyman
abdossamad-haghiri
mehdi-salmani saleh abadi
mohammad saleh-shojaei estaragh
ali-abbasi
reza-erfan arabi(araei?)
fatemeh-asgari
mohammad mahdi-gheidi
seyed mohammad pouria-momtaaze esfahani
ali-vanaki farahani
amirhosein-nedaei pour asl
parsa-hoseini
amir mohammad-imani
paniz-halvahi
amir reza-soleyman beyki
kian-omoumi
mahdiyeh-ebrahimpour khoshkedashki
sara-azarnoush
peyman-haji mohammad ebrahim
sara-zahedi movahhed
kamiyar-taeb
mohammad javad-alaedini
roya-ghavami aadel
saeid-motevali haji
hosein-partohafshojaei
arash-chaei melat shahi
hosein-mirzaei sadeghloo
"""


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, 'به بات خوش آمدید. این بات هر جمعه صبح به شما اسامی دو نفر را خواهد داد.')
    students_list = backup.split("\n")
    for i in range(0,30):
        a = []
        for i in range(0,2):
            choosen_one = random.randint(0,len(students_list)-1)
            bot.send_message(chat_id= message.chat.id , text= students_list[choosen_one])
            a.append(students_list[choosen_one])
            del students_list[choosen_one]
        # for save a list from who choosed before
        done_list = open("student_list.txt", "a+")
        myList.write(a)
        time.sleep(604800)
        # sleep for a 604800 second or a week

while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
