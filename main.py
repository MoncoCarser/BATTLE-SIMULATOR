import os, time, random


def colour_change(color):
    if color == "red":
        return ("\033[31m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "yellow":
        return ("\033[33m")
    elif color == "green":
        return ("\033[32m")
    elif color == "bold":
        return ("\033[1m")
    elif color == "purple":
        return ("\033[35m")
    elif color == "none":
        return ("\033[0m")


def main_roll(sides):
    roll_number = random.randint(1, sides)
    return roll_number


def health_roll():
    health_stat = ((main_roll(6) * main_roll(12)) / 2) + 10
    return health_stat


def strength_roll():
    strength_stat = ((main_roll(6) * main_roll(12)) / 2) + 12
    return strength_stat


def damage_roll():
    attack_damage = main_roll(6)
    return attack_damage


title_text = ("WELCOME TO")
simulator_text = ("BATTLE SIMULATOR")
name_char_1 = ("What is the name of your first fighter?")
char_1_class = ("What is your class (monk, puppy, warrior, wizard, etc.?\n")
name_char_2 = ("Our first fighter is ready. Name your secong fighter!")
filler_text = ("💀 ⚔️ 🏆   🏆 ⚔️ 💀")

#text to be centered and stats on both sides, character names on top
health_text = ("  HEALTH")
strength_text = ("STRENGTH")
special_ability_text = ("")

print()
print()
print(f"{colour_change ('bold')}{title_text: ^70}")
print()
print()
print(f"{colour_change ('bold')}{simulator_text: ^70}{colour_change('none')}")
print()
time.sleep(2)
os.system("clear")
print()
character_1_name = input(f"{name_char_1}\n\n").title()
print()
time.sleep(0.5)
character_1_class = input(f"{char_1_class}\n").lower()
print()

character_1_health = health_roll()
character_1_strength = strength_roll()

time.sleep(1)
print(
    f"Your {character_1_class} character {character_1_name}, with his hp of {character_1_health} and power of {character_1_strength} has entered the arena.")
time.sleep(1)
print()
print()
print()
# print("SECOND FIGHTER ANNOUNCING")
print()
time.sleep(1)
character_2_name = input(f"{name_char_2}\n\n").title()
print()
time.sleep(0.5)
character_2_class = input(
    "What is your class (monk, puppy, warrior, wizard, etc.?\n").lower()
print()

character_2_health = health_roll()
character_2_strength = strength_roll()

time.sleep(1)
print(
    f"Your {character_2_class} character {character_2_name}, with his hp of {character_2_health} and power of {character_2_strength} has entered the arena."
)

time.sleep(3)
os.system("clear")
announcement_text1 = (f"FIGHTERS! ENTER THE ARENA!")
announcement_text2 = (
    f"💀 {character_1_name} 💀 and {character_2_name} 💀 will battle to the DEATH 💀"
)
print()
print(f"{announcement_text1: ^70}")
print(f"{announcement_text2: ^70}")

#code moves to battle simulation phase
time.sleep(2)
os.system("clear")
round_counter = 1

while True:
    time.sleep(3)
    os.system("clear")
    print()
    text_text = (
        f"{character_1_name}        {filler_text}        {character_2_name}")
    print(f"{text_text: ^84}")
    text_text2 = (
        f"{character_1_health} ❤️       {health_text}       ❤️  {character_2_health}"
    )
    print(f"{text_text2: ^86}")
    text_text3 = (
        f"{character_1_strength} 💪       {strength_text}       💪 {character_2_strength}"
    )
    print(f"{text_text3: ^84}")
    # special ability  print(f"{text3: <10}{text3: >59}")
    print()
    print()
    print()

    battle_roll_char_1 = damage_roll()
    battle_roll_char_2 = damage_roll()

    # Atm strength and damange are not affecting as expected

    strength_difference = abs(character_2_strength - character_1_strength) + 1

    time.sleep(2)
    print(
        f"{colour_change('bold')} Begin ROUND {round_counter}!{colour_change('none')}"
    )
    print()
    time.sleep(1)
    print(
        f" {character_1_name} rolls {battle_roll_char_1} and {character_2_name} rolls {battle_roll_char_2}"
    )

    if battle_roll_char_1 < battle_roll_char_2:
        critical_roll_char_1 = main_roll(20)
        if critical_roll_char_1 == 14:
            character_1_health -= strength_difference + 10
        else:
            character_1_health -= strength_difference

        if character_1_health <= 0:
            character_1_health = 0
        print()
        time.sleep(2)
        print(f"AUCH! {character_2_name} strikes with such force!")
        print(f"HP statuses are {character_1_health} and {character_2_health}")

    elif battle_roll_char_1 > battle_roll_char_2:
        critical_roll_char_2 = main_roll(20)
        if critical_roll_char_2 == 11:
            character_2_health -= strength_difference + 10
        else:
            character_2_health -= strength_difference
        if character_2_health <= 0:
            character_2_health = 0
        print()
        time.sleep(2)
        print(f"Oh no! {character_1_name} strikes a deep wound! 🗡️")
        print(f"HP statuses are {character_1_health} and {character_2_health}")

    else:
        print()
        print("They strike with even power! ⚔️")

    if character_1_health <= 0:
        print()
        time.sleep(1)
        print(
            f"Wait! {character_1_name} has lost all his limbs and is dying an agonizing death! {character_2_name} is the victor 🏆 of this great battle! "
        )
        break
    elif character_2_health <= 0:
        print()
        time.sleep(1)
        print(
            f"WOW! {character_2_name} is down and bleeding uncontrollobly! 🩸🩸 {character_1_name} 🏆 is the victor of this great battle! "
        )
        break
    else:
        round_counter += 1
        print()
        print()
        print()
        continue
