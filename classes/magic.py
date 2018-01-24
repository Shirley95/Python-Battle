import random

class Spell:
    def __init__(self, name, cost, dmg, type): # create instance variables from variables/values that we pass in
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

        # self. - instance of class
        # Instantiation means defining or creating new object for class to access all properties like methods, fields, etc. from class.

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
