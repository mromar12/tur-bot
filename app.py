import telebot
from telebot import types

bot = telebot.TeleBot("5982549970:AAG_Dhi4N5gX9rBkarVNvt_fBHkB6qB98WE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome, Ikk! I can help you with travel tours. Please choose a tour from the menu.")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tour1 = types.KeyboardButton("Tour 1")
    tour2 = types.KeyboardButton("Tour 2")
    tour3 = types.KeyboardButton("Tour 3")
    markup.add(tour1, tour2, tour3)
    bot.send_message(message.chat.id, "Please select a tour:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Tour 1")
def tour1_info(message):
    bot.send_message(message.chat.id, "Tour 1: Grand Canyon Adventure\nDescription: Explore the beauty of the Grand Canyon with a guided tour.\nPrice: $200\nPlace: Grand Canyon National Park\nTime: 8:00 AM - 4:00 PM\nBook now:")
    book_markup = types.InlineKeyboardMarkup()
    book_button = types.InlineKeyboardButton("Book Now", callback_data="book_tour1")
    book_markup.add(book_button)
    bot.send_message(message.chat.id, "Press the button to book this tour.", reply_markup=book_markup)

@bot.callback_query_handler(func=lambda call: call.data == "book_tour1")
def book_tour1(call):
    bot.send_message(call.message.chat.id, "Please provide the following information to book Tour 1:")
    bot.send_message(call.message.chat.id, "Name:")
    bot.register_next_step_handler(call.message, process_name)

def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Surname:")
    bot.register_next_step_handler(message, process_surname, name)

def process_surname(message, name):
    surname = message.text
    bot.send_message(message.chat.id, "Age:")
    bot.register_next_step_handler(message, process_age, name, surname)

def process_age(message, name, surname):
    age = message.text
    bot.send_message(message.chat.id, "Gender:")
    bot.register_next_step_handler(message, process_gender, name, surname, age)

def process_gender(message, name, surname, age):
    gender = message.text
    bot.send_message(message.chat.id, "Are you bringing children? (Yes/No)")
    bot.register_next_step_handler(message, process_children, name, surname, age, gender)

