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

# @bot.message_handler(commands=['feed'])
# def feed(message):
#     if message.from_user.username in Pokemon.pokemons.keys():
#         pokemon = Pokemon(message.from_user.username)
#         pokemon.update()
#         bot.reply_to(message, "Ты покормил покемона!")
    
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

