#!/usr/local/bin/checkio --domain=py run the-defenders

# 
# END_DESC

# Taken from mission Army Battles

#########################################################
# Unit status


class Warrior:
    def __init__(self):
        self.NAME = "Warrior"
        self.HP = 50
        self.ATK = 5
        self.is_alive = True

    # HP:0 -> dead
    def dead(self):
        if self.HP <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self):
        self.NAME = "Knight"
        self.HP = 50
        self.ATK = 7
        self.is_alive = True


class Army:
    # Units status
    def __init__(self):
        self.residual_units = []  # Number of Units
        self.is_alive = True

    # Add units
    def add_units(self, units_name, size=1):
        if units_name == Warrior:
            self.residual_units += [Warrior] * size
        if units_name == Knight:
            self.residual_units += [Knight] * size

    # Number of Units:0 → dead
    def dead(self):
        if self.residual_units == []:
            self.is_alive = False


#########################################################
# Battle system

# 1 vs 1
def fight(unit_1, unit_2):

    # Show battle units(for test)
    # (e.g.:Warrior [ HP: 50 ] vs (P2) Warrior [ HP: 50 ])
    # print(
    #     "(P1)", unit_1.NAME,"[ HP:", unit_1.HP,"]","vs",
    #     "(P2)", unit_2.NAME,"[ HP:", unit_2.HP,"]"
    #     )

    while unit_1.is_alive:  # HP:0 -> P1 is dead
        unit_2.HP -= unit_1.ATK  # unit_1 attacks unit_2

        # Show fight progress(for test)
        # (e.g.:Warrior : 50      Warrior : 45)
        # print(unit_1.NAME, ":", unit_1.HP, "\t", unit_1.NAME, ":", unit_2.HP)

        unit_2.dead()  # Check unit HP is 0 or not
        if not unit_2.is_alive:  # HP:0 -> P2 is dead
            return True
        unit_1.HP -= unit_2.ATK

        # Display units HP(for test)
        # print(unit_1.NAME, ":", unit_1.HP, "\t", unit_2.NAME, ":", unit_2.HP)

        unit_1.dead()
    return False


# Army vs Army
class Battle:
    def __init__(self):
        pass

    def fight(self, Army_A, Army_B):
        first_fight = True
        while True:  # Loop till finish fighting
            if first_fight is True:  # Set first unit
                first_unit_A = Army_A.residual_units[0]()
                first_unit_B = Army_B.residual_units[0]()
                first_fight = False
            first_unit_A_is_survived = fight(first_unit_A, first_unit_B)
            if first_unit_A_is_survived is True:
                del Army_B.residual_units[0]  # Delete dead unit
                Army_B.dead()  # Check residual_units 0 or not
                if Army_B.is_alive is False:  # Army_B.residual_units:0 -> Army_A Win
                    return True
                first_unit_B = Army_B.residual_units[0]()  # Set next unit
            else:
                del Army_A.residual_units[0]
                Army_A.dead()
                if Army_A.is_alive is False:  # Army_A.residual_units:0 -> Army_A lose
                    return False
                first_unit_A = Army_A.residual_units[0]()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")