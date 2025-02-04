# functions_lab05.py
import random

# question 3
def collect_loot(loot_options, belt):
    print("Random loot process:")
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    print ("    |    your belt: ", belt)
    return loot_options, belt

# question 4 Use loot
def use_loot(belt, health_option):
    good_loot_options = ["Health Potion", "Magic Sword"]
    bad_loot_options = ["Poison"]

    print("you see a monster! so you quickly use first item:")

    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_option = min(20, (health_option + 2))
        print("You used " + first_item + " and your health is " + str(health_option))
    elif first_item in bad_loot_options:
        health_option = max(20, (health_option - 2))
        print("You used " + first_item + " and your health is " + str(health_option))
    else:
        print("You used " + first_item + " but its not effective")
    return belt, health_option