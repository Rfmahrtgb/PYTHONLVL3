import telebot
from config import token
from random import choice, randint, sample
import string

API_TOKEN = token  

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am BibobBot.
I veryveryveryvery cool! I universal. Just tell me and I'll do it. Write "/info" and you see my skills.\
""")
    
@bot.message_handler(commands=['info'])
def info_handler(message):
    bot.reply_to(message, """\
My skills/commands:
/coin
/joke
/password
/instructor(может дать инструкции по рисовке: бабочка, солнце, дерево. Просто напишите боту на какой предемет вы хотите инструкцию например "дерево". Не пишите название команды напишите предмет тот на который хотите увидеть инструкцию. )
""")
    
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice([
        "Колобок повесился",
        "Рыба утонула",
        "Бабушка так быстро и сильно мешала борщ, что воронка начала засасывать мебель в квартире.",
        "Можно бесконечно долго смотреть на три вещи по цене двух, задаваясь вопросом: «Зачем я это купил?!»"
    ])
    bot.reply_to(message, joke)

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['password'])
def password_handler(message):
    length = randint(8, 12)  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(sample(characters, length))
    bot.reply_to(message, f"Ваш сгенерированный пароль: {password}")

@bot.message_handler(func=lambda message: True)
def handle_instruction_request(message):
    topic = message.text.lower()
    
    instructions = {
        "бабочка": """\
Как нарисовать бабочку:
1. Начните с рисования верхней части крыльев в форме полукруга.
2. Добавьте нижнюю часть крыльев, сделав их более округлыми.
3. Соедините верхние и нижние части крыльев с помощью изогнутых линий.
4. Нарисуйте тело бабочки между крыльями.
5. Добавьте детали на крыльях: узоры и точки.
6. Раскрасьте бабочку яркими цветами.""",
        
        "солнце": """\
Как нарисовать солнце:
1. Нарисуйте круг в центре страницы.
2. Добавьте лучи вокруг круга: прямые линии или волнистые.
3. Раскрасьте солнце желтым или оранжевым цветом.""",
        
        "дерево": """\
Как нарисовать дерево:
1. Нарисуйте ствол дерева: две параллельные линии вниз.
2. Добавьте ветви: изогнутые линии от ствола.
3. Нарисуйте листву: круглые или овальные формы на конце ветвей.
4. Раскрасьте ствол коричневым, а листву зеленым.""",
    }
    
    if topic in instructions:
        bot.reply_to(message, instructions[topic])
    else:
        bot.reply_to(message, "Извините, я не знаю как это нарисовать. Попробуйте что-то другое.")

bot.infinity_polling()

print("hi")