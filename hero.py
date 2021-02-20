from ability import Ability
from armor import Armor
from weapon import Weapon
import random


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
        # using append method to add ability objects to the list

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        # appending the weapon object passed in as an
        # argument to self.abilities.

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

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
        after_damage = damage - self.defend()
        self.current_health -= after_damage

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        winner = random.choice([self, opponent])
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return f'Draw'
        else: 
            while self.is_alive() and opponent.is_alive():
                damage_amount = self.attack()
                opponent.take_damage(damage_amount)
                damage_amount = opponent.attack()
                self.take_damage(damage_amount)
            if self.is_alive():
                winner = self
            elif opponent.is_alive():
                winner = opponent
            else:
                return f'Draw'

        return f'{winner.name} Won!'


        # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight


if __name__ == "__main__":

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 30)
    # ability2 = Ability("Super Eyes", 40)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # print(hero1.fight(hero2))

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())