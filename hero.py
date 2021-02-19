from ability import Ability
from armor import Armor
import random


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        self.abilities.append(ability)
        # using append method to add ability objects to the list

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        # looping through all of the hero's abilities
        # and returning the total damage
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        after_damage = self.defend() - damage
        self.current_health += after_damage

    def is_alive(self):
        pass

    def fight(self, opponent):
        winner = random.choice([self, opponent])
        return f'{winner.name} Won!'


if __name__ == "__main__":

    # my_hero = Hero("Grace Hopper", 200)
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # print(hero1.fight(hero2))
    # ability = Ability("Great Debugging", 50)
    # ability2 = Ability('Dancing', 32)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(ability2)
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

    
    