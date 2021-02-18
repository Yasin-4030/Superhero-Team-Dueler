import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        winner = random.choice(self.name)
        return f'{winner} Won!'


if __name__ == "__main__":

    my_hero = Hero("Grace Hopper", 200)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)