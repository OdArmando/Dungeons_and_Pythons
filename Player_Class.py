class Player:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.inventory = []


class Warrior(Player):
    def __init__(self):
        super().__init__("Warrior", 9000, 2000)


class Sorcerer(Player):
    def __init__(self):
        super().__init__("Sorcerer", 2500, 5000)


class Healer(Player):
    def __init__(self):
        super().__init__("Healer", 8000, 7000)
