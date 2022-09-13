class Enemy:
    def __init__(self, name):
        self.name = name

    def Goblin(self, name):
        self.name = name
        self.life = 800
        self.damage = 800

    def Orc(self, name):
        self.name = name
        self.life = 1200
        self.damage = 1100

    def Troll(self, name):
        self.name = name
        self.life = 2000
        self.damage = 2500