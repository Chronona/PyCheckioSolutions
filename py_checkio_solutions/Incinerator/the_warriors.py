#!/usr/local/bin/checkio --domain=py run the-warriors

# 
# END_DESC

class Warrior:
    attack = 5

    def __init__(self):
        self.health = 50

    @property
    def is_alive(self):
        return self.health >= 0


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            return True
        unit_1.health -= unit_2.attack
        if not unit_1.is_alive:
            return False