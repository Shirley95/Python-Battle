from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random
'''
Initialization means assigning initial value to variables after declaring or while declaring. All variables are always given an initial value at the point the variable is declared. Thus, all variables are initialized.

Instantiation means defining or creating new object for class to access all properties like methods, fields, etc. from class.
'''
# dot method, ., calls a method i.e. .sort() is a method; calls a method that has already instantiated


# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999) # heal for max hp therefore a random number will do
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spell = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_item = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
               {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
               {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]


# Instantiate People (class)
player1 = Person("Valos: ", 3260, 132, 300, 34, player_spell, player_item) # instantiating the Person class, this instance of class going into player
player2 = Person("Kula:  ", 4160, 188, 311, 34, player_spell, player_item)
player3 = Person("Robot: ", 3089, 174, 288, 34, player_spell, player_item)

enemy1 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, []) # henchmen
enemy2 = Person("Magus", 11200, 701, 525, 25, enemy_spells, []) # able to access different variables, main enemy
enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

#when the program first starts, an enemy starts
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
# wrap color around a certain text - we need to end it as well i.e. ENDC
# realise the format of how the statement is written and ended with ENDC, after that text becomes normal

while running:
    print("=====================")

    print("\n\n")
    print("NAME                   HP                                       MP")
    for player in players:
        player.get_stats() # get hp/mp scores for players

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats() # get enemy's hp/mp scores

    for player in players:

        player.choose_action()
        choice = input("    Choose action: ") # prompt(cause) for input

        index = int(choice) - 1 # actions begins at 1 but code starts to count from 0

        if index == 0: # if index is 0 then we have chosen to attack , need to generate damage
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been slayed!")
                del enemies[enemy]

        elif index == 1:
            # allow player use magic
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1: #allowing to go back in menu if selected the wrong choice/choice doesn't exist
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg) # ask enemy to take the magic damage

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been slayed!")
                    del enemies[enemy]
        # if player chose item
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
            # statement at line 90 placed aboved statement at line 94; when item 1 left will become 0 as it will deduct
            player.items[item_choice]["quantity"] -= 1

            '''item_quantity = player.items[item_choice]["quantity"]
            # stored RHS value in another variable we modified the variable we created, but we didn't modify "quantity" itself        
            item_quantity -= 1'''

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer": # creating full heal for all members' when using this portion
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack": # attack type is grenade
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop) # item.prop: damage value of prop

                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name.replace + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been slayed!") # replacing whitespace in enemy's name
                    del enemies[enemy]

    # Check if battle is over by confirming HP = 0
    '''defeated_enemies = 0
    defeated_players = 0  # setting to 0 therefore same person dead doesn't not keep adding as it gets back to 0 for every loop the while loop runs

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "Your enemies has been slayed! You win!" + bcolors.ENDC)
        running = False  # exiting the loop

    #Check if Enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "K.O. Your enemies have defeated you!" + bcolors.ENDC)
        running = False'''

    print("\n")
    # Enemy attack phase
    for enemy in enemies: # allowing all enemies to attack instead of one; choosing their opponent randomly
        enemy_choice = random.randrange(0, 2) # enemies' choice to use which type of attack ie. attack/magic/item against players

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 3) # initialised here therefore cannot used elsewhere unless global
            # enemy generating damage to any player based on target
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg) # players[target] target any player in players array
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == 'white': # allowing enemy to use white magic to heal
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + "for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg) # ask random player to take the magic damage that was passed on

                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has been slayed!")
                    del players[player]
            #print("Enemy chose", spell, "damage is", magic_dmg)

    for n in enemies:
        if len(enemies) <= 1:
            print("Your enemies has been slayed! You win!")
            running = False

    for j in players:
        if len(players) <= 1:
            print("You lose! Your team lost.")
            running = False

'''
A variable which is defined inside a function is local to that function. It is accessible from the point at which it is defined 
until the end of the function, and exists for as long as the function is executing. 
'''


