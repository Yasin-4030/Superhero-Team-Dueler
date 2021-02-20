import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        half_damage = self.max_damage // 2
        random_value = random.randint(half_damage, self.max_damage)
        return random_value

    