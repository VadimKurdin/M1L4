import telebot 
from config import token
from logic import Pokemon, Fighter, Wizard
import random
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():

        chance = random.randint(1, 100)
        if chance >=50:
            pokemon = Wizard(message.from_user.username)
        else:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed_pok(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        response = pok.feed()
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "У вас нет покемона.")

@bot.message_handler(commands=['info'])
def info(message):
    # if message.reply_to_message:
    #     if message.reply_to_message.from_user.username in Pokemon.pokemons.keys():
    #         bot.send_message(message.chat.id, Pokemon.pokemons.get(message.reply_to_message.from_user.username).info())
    #         bot.send_photo(message.chat.id, Pokemon.pokemons.get(message.reply_to_message.from_user.username).show_img())
    # else: 
    if message.from_user.username in Pokemon.pokemons.keys():
        bot.send_message(message.chat.id, Pokemon.pokemons.get(message.from_user.username).info())
        bot.send_photo(message.chat.id, Pokemon.pokemons.get(message.from_user.username).show_img())

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        fighter_1=message.from_user.username
        fighter_2=message.reply_to_message.from_user.username
        if fighter_1 in Pokemon.pokemons.keys() and fighter_2 in Pokemon.pokemons.keys():
            pokemon1=Pokemon.pokemons.get(fighter_1)
            pokemon2=Pokemon.pokemons.get(fighter_2)
            bot.send_message(message.chat.id, Pokemon.pokemons.get(fighter_1).attack(Pokemon.pokemons.get(fighter_2)))
            if pokemon1.hp<=0:
                del Pokemon.pokemons[fighter_1]
            if pokemon2.hp<=0:
                del Pokemon.pokemons[fighter_2]
bot.infinity_polling(none_stop=True)

