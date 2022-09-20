from Player_Class import Player
class Item(object):
    def __init__(self, name, defence, damage, type):
        self.name = name
        self.defence = defence
        self.damage = damage
        self.type = type
    def itemadd(self):
