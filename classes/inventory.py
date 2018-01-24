# adding items

class Item:
    # the item class: going to have name, type, description and prop
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
