# DEV 108 Character Generator
# 07/29/2026
# Doug Babcock

import random
def generate_character(name):
    """Generate a random character and return it."""

    # Generate base stats
    strength = random.randint(8, 16)
    intellect = random.randint(8, 16)
    constitution = random.randint(8, 16)
    wisdom = random.randint(8, 16)
    dexterity = random.randint(8, 16)

    classes = ["Fighter", "Wizard", "Rogue"]
    races = ["Human", "Elf", "Dwarf", "Halfling"]
    race = random.choice(races)
    character_class = random.choice(classes)

    # Add race bonuses
    if race == "Elf":
        intellect += 2
    elif race == "Dwarf":
        constitution += 2
    elif race == "Halfling":
        dexterity += 2
    elif race == "Human":
        strength += 1
        dexterity += 1
        constitution += 1
        intellect += 1
        wisdom += 1

    # Bonuses
    strength_bonus= (strength - 10) // 2
    dexterity_bonus = (dexterity - 10) // 2
    intellect_bonus = (intellect - 10) // 2
    saving_throw = (wisdom - 10) // 2   # Wizard casts magic missile
    constitution_bonus = (constitution - 10) // 2
    damage_bonus = 0    # This will make damage calcualtion easier
    initiative = dexterity_bonus
    armor_class = 10 + dexterity_bonus

    # Calculate class features
    if character_class == "Fighter":
        hit_points = 10 + constitution_bonus
        damage_bonus = strength_bonus
        armor_class += 2
    elif character_class == "Wizard":
        hit_points = 6 + constitution_bonus
        damage_bonus = intellect_bonus + 1
    elif character_class == "Rogue":
        hit_points = 8 + constitution_bonus
        damage_bonus = dexterity_bonus
        initiative += 2

    return {
        "name": name,
        "class": character_class,
        "race": race,
        "strength": strength,
        "dexterity": dexterity,
        "constitution": constitution,
        "intellect": intellect,
        "wisdom": wisdom,
        "hit_points": hit_points,
        "damage_bonus": damage_bonus,
        "initiative": initiative,
        "armor_class": armor_class,
        "saving_throw": saving_throw,
        "max_hit_points": hit_points
    }

def print_character(character):
    """Prints the character's stats."""
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃            CHARACTER SHEET                 ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ Name         : {character['name']:<28}┃")
    print(f"┃ Class        : {character['class']:<28}┃")
    print(f"┃ Race         : {character['race']:<28}┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ STR          : {character['strength']:<28}┃")
    print(f"┃ DEX          : {character['dexterity']:<28}┃")
    print(f"┃ CON          : {character['constitution']:<28}┃")
    print(f"┃ INT          : {character['intellect']:<28}┃")
    print(f"┃ WIS          : {character['wisdom']:<28}┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ HP           : {character['hit_points']:<28}┃")
    print(f"┃ Damage Bonus : {character['damage_bonus']:<28}┃")
    print(f"┃ Initiative   : {character['initiative']:<28}┃")
    print(f"┃ Armor Class  : {character['armor_class']:<28}┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def battle(character, enemy):
    """Simulates a battle between the character and an enemy."""
    print("*" * 46)
    print(f"Battle begins between {character['name']} and {enemy['name']}!")
    print()

    # Roll for initiative
    character_initiative = roll(20) + character['initiative']
    enemy_initiative = roll(20) + enemy['initiative']
    print(f"{character['name']} (initiative: {character_initiative}) vs {enemy['name']} (initiative: {enemy_initiative})")
    if character_initiative >= enemy_initiative:
        print(f"{character['name']} goes first!")
        first = character
        second = enemy
    else:
        print(f"{enemy['name']} goes first!")
        first = enemy
        second = character
    first_potions = 2
    second_potions = 2
    round = 1

    while character['hit_points'] > 0 and enemy['hit_points'] > 0:
        # Display battle status
        print("=" * 46)
        print(f"           ⚔️    ROUND {round}   ⚔️               ")
        print("=" * 46)
        print(f"{character['name']}      vs {enemy['name']} ")
        print(f"HP: {character['hit_points']}/{character['max_hit_points']}           HP: {enemy['hit_points']}/{enemy['max_hit_points']}")
        print()

        # First player's turn - first check if we should use a potion
        if first['hit_points'] < first['max_hit_points'] and random.choice([True, False]) and first_potions > 0:
            first = use_potion(first)
            first_potions -= 1
            print(f"{first['name']} uses a potion and regains some health!")
        # If we don't use a potion, we attack
        else:
            d20 = roll(20)
            damage = calculate_damage(first, second, d20)
            print(f"{first['name']} rolls a {d20} for the attack!")
            if damage == 0:
                print("The attack missed!")
            else:
                second['hit_points'] -= damage
                print(f"{first['name']} hits {second['name']} for {damage} damage!")
                if second['hit_points'] <= 0:
                    print(f"{second['name']} has been defeated!")
                    break
        print()

        # Second player's turn
        if second['hit_points'] < second['max_hit_points'] and random.choice([True, False]) and second_potions > 0:
            second = use_potion(second)
            second_potions -= 1
            print(f"{second['name']} uses a potion and regains some health!")
        else:
            d20 = roll(20)
            print(f"{first['name']} rolls a {d20} for the attack!")
            damage = calculate_damage(second, first, d20)
            if damage == 0:
                print(f"{second['name']} misses {first['name']}!")
            else:
                first['hit_points'] -= damage
                print(f"{second['name']} hits {first['name']} for {damage} damage!")
                if first['hit_points'] <= 0:
                    print(f"{first['name']} has been defeated!")
                    break
        print()
        round += 1

def calculate_damage(attacker, defender, d20):
    """Returns damage dealt; Returns 0 for a miss"""

    # Wizard does spell damage, so we check for saving throws
    if attacker['class'] == "Wizard":
        spell_dc = 10 + abilityModifier(attacker['intellect'])
        save_roll = roll(20) + defender['saving_throw']
        if save_roll >= spell_dc:
            # Defender makes saving throw
            return 0
        else:
            return roll(6) + attacker['damage_bonus']

    # Everyone else makes attack rolls, but fighters use str and rogues use dex
    if attacker['class'] == "Fighter":
        if d20 + abilityModifier(attacker['strength']) >= defender['armor_class']:
            return roll(4) + attacker['damage_bonus']
    elif attacker['class'] == "Rogue":
        if d20 + abilityModifier(attacker['dexterity']) >= defender['armor_class']:
            return roll(4) + attacker['damage_bonus']
    return 0
    
def use_potion(character):
    """Uses a potion to restore health."""
    healing = roll(6)
    # We accidentally over healed - fixed!
    if character['hit_points'] + healing > character['max_hit_points']:
        healing = character['max_hit_points'] - character['hit_points']
    character['hit_points'] += healing
    return character

def roll(n):
    """Rolls a n-sided die."""
    return random.randint(1, n)

# added this after realizing my attack modifiers were wonky in calculate_damage()
# I'm not modifying generate_character() to use this instead
def abilityModifier(ability_score):
    """Returns the ability modifier for a given ability score."""
    return (ability_score - 10) // 2

def getyesno(message):
    while True:
        response = input(message).lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print(r"""
         ____        ____    ____        _   _   _        ____  _           
        |  _ \ _ __ |  _ \  | __ )  __ _| |_| |_| | ___  / ___|(_)_ __ ___  
        | | | | '_ \| | | | |  _ \ / _` | __| __| |/ _ \ \___ \| | '_ ` _ \ 
        | |_| | | | | |_| | | |_) | (_| | |_| |_| |  __/  ___) | | | | | | |
        |____/|_| |_|____/  |____/ \__,_|\__|\__|_|\___| |____/|_|_| |_| |_|
                                                        __----~~~~~~~~~~~------___
                                        .  .   ~~//====......          __--~ ~~
                        -.            \_|//     |||\\  ~~~~~~::::... /~
                    ___-==_       _-~o~  \/    |||  \\            _/~~-
            __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
        _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
        .~       .~       |   \\ -_    /  /-   /   ||      \   /
        /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
        |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
                '         ~-|      /|    |-~\~~       __--~~
                            |-~~-_/ |    |   ~\_   _-~            /\
                                /  \     \__   \/~                \__
                            _--~ _/ | .-~~____--~-/                  ~~==.
                            ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                        -_     ~\      ~~---l__i__i__i--~~_/
                                        _-~-__   ~)  \--______________--~~
                                    //.-~~~-~_--~- |-------~~~~~~~~
                                            //.-~~~--\
            """)
    # Get names and generate a character
    enemy_names = ["Trogdor", "Mantaur", "Brigand", "Pirate", "Ninja"]
    default_names = ["Profontius Crumjacks", "Horatio Buttkicker", "Gilbert Swordfists", "Reginald Snifflebottom"]
    play = getyesno("Would you like to create a character? ")

    while play:
        name = input("Enter your character's name: ")
        if name == "":
            name = random.choice(default_names)
            character = generate_character(name)
        else:
            character = generate_character(name)
        print()
        print("Your character:")
        print_character(character)
        enemy = generate_character(random.choice(enemy_names))
        print()
        if not getyesno("Do you accept this character? "):
            print("Generating a new character...")
            print()
            continue
        print()
        print("You are walking through the forest when you encounter a " + enemy['name'] + "!")
        print_character(enemy)
        print()
        input("There's no way out! Press enter to begin the battle...")
        battle(character, enemy)

        play = getyesno("Would you like to create a different character? ")

if __name__ == "__main__":
    main()