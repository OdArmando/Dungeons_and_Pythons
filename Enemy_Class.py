class Enemy:
    def __init__(self, name, life, attack_power):
        self.name = name
        self.life = life
        self.attack_power = attack_power


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 1000, 500)


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 1200, 1100)


class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 2000, 2500)
