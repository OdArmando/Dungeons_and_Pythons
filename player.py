"""The player module, all classes are stored with all the information about power and items"""
import random


class Player:
    """The Player main class"""

    def __init__(self, name, hp, power, defence, weapon, armor):
        self.hp = hp
        self.name = name
        self.power = power
        self.defence = defence
        self.weapon = weapon
        self.armor = armor

    def attack(self, user):
        """The attack sequence used in fighting scene"""
        if self.power <= user.defence:
            user.hp = user.hp
            user.defence -= 5
        else:
            user.hp -= self.power - user.defence
            user.defence -= 5

    def gear_up(self):
        """Method after player opens chest and new stats are given"""
        self.power += self.weapon
        self.defence += self.armor

    def open_chest(self):
        """Stats random after opening chest"""
        self.weapon = random.randrange(100, 500, 50)
        self.armor = random.randrange(10, 100, 10)


class Wizard(Player):
    """The Wizard class with all the information and stats"""

    def __init__(self, name, hp=500, power=150, defence=30, weapon=200, armor=20):
        super().__init__(name, hp, power, defence, weapon, armor)
        self.weapon_type = 'orb'
        self.armor_type = 'robe'
        self.type_of = 'wizard'


class Knight(Player):
    """The Knight class with all the information and stats"""

    def __init__(self, name, hp=800, power=60, defence=60, weapon=100, armor=40):
        super().__init__(name, hp, power, defence, weapon, armor)
        self.weapon_type = 'sword'
        self.armor_type = 'armor'
        self.type_of = 'knight'


class Cleric(Player):
    """The Cleric class with all the information and stats"""

    def __init__(self, name, hp=700, power=70, defence=50, weapon=130, armor=30):
        super().__init__(name, hp, power, defence, weapon, armor)
        self.weapon_type = 'staff'
        self.armor_type = 'cape'
        self.type_of = 'cleric'
