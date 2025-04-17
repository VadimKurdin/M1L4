from random import randint
import requests
import random
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = int(self.get_attack())
        self.hp = int(self.get_hp())
        self.level = 0
        Pokemon.pokemons[pokemon_trainer] = self
    
    # Метод для получения картинки покемона через API


    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if int(data['stats'][1]["base_stat"])/2>=100:
                return str(data['stats'][1]["base_stat"]) + ' У вас очень сильный покемон!'
            return int(data['stats'][1]["base_stat"])/2
        else:
            return "Pikachu"

    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]["base_stat"])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def update(self):
        self.level +=1
    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покемона: {self.name}
        Атака твоего покемона: {self.power}
        Здоровье твоего покемона: {self.hp}"""
    

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = random.randint(1,100)
            if chance <= enemy.magic_chance:
                return f"Покемон-волшебник @{enemy.pokemon_trainer} применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            if isinstance(self, Wizard): 
                chance = random.randint(1,100)
                if chance <= self.magic_chance:
                    return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"+f"Покемон-волшебник @{self.pokemon_trainer} применил щит в сражении"
            self.hp -= enemy.power
            if self.hp <= 0:
                self.hp = 0
                return f"Победа @{enemy.pokemon_trainer} над @{self.pokemon_trainer}! "
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = random.randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец @{self.pokemon_trainer} применил супер-атаку силой:{super_power} "
    def info(self):
        return f"""У тебя покемон боец 
        """ + super().info()

class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.magic_chance=40
    def attack(self, enemy):
        return super().attack(enemy)
    def info(self):
        return f"""У тебя покемон волшебник 
        """ + super().info()