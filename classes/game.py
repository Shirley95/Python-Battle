import random

import pprint


# assigning variables to colours

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[94m'


class Person:
    # setting a bunch of instance variables
    # mp = magic points, hp = hit points, df = defence
    def __init__(self, name, hp: object, mp, atk, df, magic, items): # instantiation of objects
        self.maxhp = hp # max hp; don't want to over-heal
        self.hp = hp  # current hp; going to change throughout battle
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10 # based on what's passed on atk
        self.df = df
        self.magic = magic # magic object is been passed in as dictionary: different magoc and mp cost
        self.items = items
        self.actions = ["Attack", "Magic", "Items"] # displayed as it prompts us when it is our turn
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) # self.atkl as inside of a class
    # enemies attacking us; generate the amount of damage, want to be more dynamic

    # create function for enemy to take damage
    def take_damage(self, dmg): # passing damage number into this function
        # subtract the amount of damage from current hp
        self.hp -= dmg
        if self.hp < 0: # self-checking otherwise code will think hp is either 0 or higher
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost): # reduce magic points that we have because of its cost
        self.mp -= cost

    '''def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"] '''

    # need to way to choose the actions; magic/attack

    def choose_action(self):
        i = 1 # want option to start with one
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("         " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic: # list of magic is passed in Person instance and then to self.magic
            print("         " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            # print spell name and cost of spell
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("         " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            '''no need to call dictionary name as player_item is passed in Person instance and is considered as items in Person instance. This 
            is passed to instantiation of Person class as self.items. Using loop on self.items gives us access to player_item
            '''
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp != 0:
                print("        " + str(i) + ".", enemy.name ) # printing which enemy we are targeting
                i += 1
        choice = int(input("    Choose target:")) -1 # choosing which enemy to target, array starts at index 0 therefore -1 since choosing target starts at 1
        return choice

    def get_enemy_stats(self): # hp/mp bar for enemy
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2 # progress of 50 characters

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""  # variable figured how many whitespaces need to proceed it and put it in - stuffing we need including hp_string

        if len(hp_string) < 11:  # length of HP digits including slash is 9
            decreased = 11 - len(hp_string)  # contains variable of hwo many digits are left

            while decreased > 0:
                current_hp += " "  # increase whitespace as digits become less
                decreased -= 1  # decrease in digits

            current_hp += hp_string
        else:
            current_hp += hp_string

        print("                        __________________________________________________")
        print(bcolors.BOLD + self.name + "      " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")
        # self.mp/hp need to be a str type to be accessible here as self.mp/hp is int type

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp) * 100 / 4 #i.e divide by 25

        mp_bar = ""
        mp_ticks = (self.mp/self.maxmp) * 100 /10

        while bar_ticks > 0: # updating the hp bar
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25: # increasing the number of whitespace as hp decreases
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"  #increasing the hp block whilst number of whitespace
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = "" # variable figured how many whitespaces need to proceed it and put it in - stuffing we need including hp_string

        if len(hp_string) < 9: #length of HP digits including slash is 9
            decreased = 9 - len(hp_string)  # contains variable of hwo many digits are left

            while decreased > 0:
                current_hp += " " # increase whitespace as digits become less
                decreased -= 1 # decrease in digits

            current_hp += hp_string
        else:
            current_hp += hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp += mp_string


        print("                        _________________________               __________")
        print(bcolors.BOLD + self.name +"      " +
              current_hp +" |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +"|     " +
              current_mp +" |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
                # self.mp/hp need to be a str type to be accessible here as self.mp/hp is int type

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        # percentage of hit points
        #pct = self.hp / self.maxhp * 100

        # Chooses the spell again only if: if spell cost bigger than magic points or orignally chose white magic and % of hp is over 50
        if (self.mp < spell.cost): # or (spell.type == "white" and pct > 50):
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
