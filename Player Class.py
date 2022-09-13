class Player:
    def __init__(self, name, hp, mana, inventory):
        self.name = name
        self. hp = hp
        self.mana = mana
        self.inventory = inventory
    def Attack(self):
        if Player == Warrior:
            damage = 2000


class Warrior(Player):
    def __init__(self, name):
        self.name = name
        self.hp = 9000
        self.mana = 2000

class Sorcerer(Player):
    def __init__(self, name):
        self.name = name
        self. hp = 2500
        self.mana = 5000

class Healer(Player):
    def __init__(self,name):
        self.name = name
        self.hp = 10000
        self.mana = 7500

