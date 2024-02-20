# import telebot
#
# bot = telebot.TeleBot("6853034209:AAFsyRbjaeLBBsgqP5hYFGeOC_9IAPqfBYM")
#
# @bot.message_handler(commands=['start']) def start(message): """Отправляет приветственное сообщение и предлагает
# выбрать язык.""" bot.send_message(message.chat.id, "Здравствуйте! Вас приветствует Агенство проектного управления
# Приморского края.") bot.send_message(message.chat.id,"Чем мы можем вам помочь?")
#
# from telebot import types
#
# keyboard = types.ReplykeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#
# # Добавление кнопоки на клавиатуу
# button1 = types.keyboardButton("Кнопк1")
# button2 = types.keyboardButton("Кнопк2")
# keyboard.add(button1, button2)
#
# # Отправьте сообщение с клавиатуой
# bot.send_message(chat_id, "Выберите один из вариантов:", reply_keyboard=keyboard)

# import sqlite3
#
# # Создаем соединение с базой данных
# connect = sqlite3.connect("ranking12_23.db")

# Создаем курсор
# cursor = connect.cursor()
#
# row_name = input("Выберите орган исполнительной власти: ")
#
# # Выполняем запрос к базе данных
# cursor.execute(f'SELECT * FROM ranking_oiv WHERE name = ?', (row_name,))
#
# # Получаем результат запроса
# result = cursor.fetchall()
#
# # Формируем сообщение для чат-бота
# message = ""
# for row in result:
#     message += f"{row[1]}\n"
#     message += f"РП в составе НП: {row[2]}\n"
#     message += f"РП вне НП: {row[3]}\n"
#     message += f"Указ 68: {row[4]}\n"
#     message += f"Инвестиционный климат: {row[5]}\n"
#     message += f"АИП: {row[6]}\n"
#     message += f"Стратегические проекты: {row[7]}\n"
#     message += f"НСИ: {row[8]}\n"
#     message += f"Ведомственные проекты: {row[9]}\n\n"
# if result:
#     print(message)
# else:
#     print("Ошибка, вернитесь в главное меню и попробуйте еще раз.")

# bot.polling()

import telebot
from telebot import types  # для указание типов
import sqlite3

bot = telebot.TeleBot("6853034209:AAFsyRbjaeLBBsgqP5hYFGeOC_9IAPqfBYM")


# row_name = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Рейтинг")
    btn2 = types.KeyboardButton("ИСУП")
    btn3 = types.KeyboardButton("FAQ")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}! Вас приветствует Агентство проектного управления Привиского "
                          "края".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Чем мы можем вам помочь?".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    # global row_name
    if message.text == "ИСУП":
        bot.send_message(message.chat.id, text="Этот раздел в разработке")

    if message.text == "FAQ":
        bot.send_message(message.chat.id, text="Этот раздел в разработке")

    if message.text == "Рейтинг":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Органы исполнительной власти")
        btn2 = types.KeyboardButton("Кураторы и руководители")
        btn3 = types.KeyboardButton("Проекты")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите из предложенных вариантов ниже", reply_markup=markup)

    if message.text == "Органы исполнительной власти":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton(
            "Агентство по гидротехническим сооружениям, мелиорации и гидрологии Приморского края")
        btn2 = types.KeyboardButton("Министерство сельского хозяйства ПК")
        btn3 = types.KeyboardButton("Агентство проектного управления ПК")
        btn4 = types.KeyboardButton("Министерство лесного хозяйства и охраны объектов животного мира ПК")
        btn5 = types.KeyboardButton("Министерство строительства ПК")
        btn6 = types.KeyboardButton("Министерство физической культуры и спорта ПК")
        btn7 = types.KeyboardButton("Министерство жилищно-коммунального хозяйства ПК")
        btn8 = types.KeyboardButton("Министерство образования ПК")
        btn9 = types.KeyboardButton("Министерство профессионального образования и науки населения ПК")
        btn10 = types.KeyboardButton("Агентство по туризму ПК")
        btn11 = types.KeyboardButton("Министерство транспорта и дорожного хозяйства ПК")
        btn12 = types.KeyboardButton("Министерство имущественных и земельных отношений ПК")
        btn13 = types.KeyboardButton("Министерство сельского хозяйства ПК")
        btn14 = types.KeyboardButton("Государственная жилищная инспекция ПК")
        btn15 = types.KeyboardButton(
            "Министерство по делам гражданской обороны, защиты от чрезвычайных ситуаций и ликвидации последствий "
            "стихийных бедствий ПК")
        btn16 = types.KeyboardButton("Министерство труда и социальной политики ПК")
        btn17 = types.KeyboardButton("Министерство цифрового развития и связи ПК")
        btn18 = types.KeyboardButton("Департамент по делам молодежи ПК")
        btn19 = types.KeyboardButton("Министерство здравоохранения ПК")
        btn20 = types.KeyboardButton("Министерство культуры и архивного дела ПК")
        btn21 = types.KeyboardButton("Министерство промышленности и торговли ПК")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17, btn18, btn19, btn20, btn21)
        bot.send_message(message.chat.id, text="Выберите нужный орган исполнительной власти", reply_markup=markup)


connect = sqlite3.connect("ranking12_23.db")
cursor = connect.cursor()


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    bot.send_message(message.chat.id, text="Ваш запрос в обработке...")
    row_name = input(message)

    cursor.execute(f'SELECT * FROM ranking_oiv WHERE name = ?', (row_name,))
    result = cursor.fetchall()

    message1 = ''
    for row in result:
        message1 += f"Название: {row[1]}\n"
        message1 += f"РП в составе НП: {row[2]}\n"
        message1 += f"РП НП: {row[3]}\n"
        message1 += f"Указ 68: {row[4]}\n"
        message1 += f"Инновационный климат: {row[5]}\n"
        message1 += f"АИП: {row[6]}\n"
        message1 += f"Стратегические проекты: {row[7]}\n"
        message1 += f"НСИ: {row[8]}\n"
        message1 += f"Ведомственные проекты: {row[9]}\n\n"

    if result:
        bot.send_message(message.chat.id, text=message)


connect.commit()
cursor.close()
connect.close()

bot.polling(none_stop=True, interval=1)
