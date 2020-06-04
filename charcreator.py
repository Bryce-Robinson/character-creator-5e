PYTHONDONTWRITEBYTECODE=" "
import random, time, classes
#lists
list_name = ["race", "class"]
races = ["Human", "Elf", "Dwarf", "Gnome", "Halfling", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling"]
races_subraces ={"Human":[], "Elf":["High Elf", "Wood Elf", "Drow"], "Dwarf":["Hill Dwarf", "Mountain Dwarf"], "Gnome":["Forest", "Rock"], "Halfling":["Lightfoot", "Stout"], "Dragonborn":[], "Half-Elf":[], "Half-Orc":[], "Tiefling":[]}

class_ = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
class_subclass = {"Barbarian":["Path of the Berzerker", "Path of the Totem Warrior"], "Bard":["College of Lore", "College of Valor", "College of Shadows"], "Cleric":["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain","Warrior Domain"], "Druid":["Circle of the Land", "Circle of the Moon"], "Fighter":["Champion", "Battle Master", "Eldritch Knight"], "Monk":["Way of the Open Hand", "Way of the Shadow", "Way of the 4 Elements"], "Paladin":["Oath of Devotion","Oath of the Ancients", "Oath of Vengeance"], "Ranger":["Hunter", "Beastmaster"], "Rogue":["Thief", "Assasin", "Arcane Trickster"], "Sorcerer":["Draconic Bloodline", "Wild Magic"], "Warlock":["Pact of the Chain", "Pact of the Blade", "Pact of the Tome"], "Wizard":["School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Necromancy", "School of Transmutation"]} 


#variables
welcome_message = "Welcome to the Dungeon's and Dragons Command-line Character Generator!\nFor the sake of simplicity and realistic common characters this program will only be using content from the Players Handbook. \nIf you want to create specific characters from the other expansions then you will have to use something else."
#AT THE END UNCOMMENT BELOW FOR THE SPLASH SCREEN THING
#print("                                                       ")
#print("  ____________     _____    _____      ____________    ")
#print("  \           \   |\    \   \    \     \           \   ")
#print("   \           \   \\\    \   |    |     \           \  ")
#print("    |    /\     |   \\\    \  |    |      |    /\     | ")
#print("    |   |  |    |    \|    \ |    |      |   |  |    | ")
#print("    |    \/     |     |     \|    |      |    \/     | ")
#print("   /           /|    /     /\      \    /           /| ")
#print("  /___________/ |   /_____/ /______/|  /___________/ | ")
#print(" |           | /   |      | |     | | |           | /  ")
#print(" |___________|/    |______|/|_____|/  |___________|/   ")
#print("                                                       ")

#--------------------------------------------------------------FUNCTIONS--------------------------------------------------------------------------

#function iterates through a prestored list and should create an output that looks something like [1] Human [2] Elf [3] Dwarf [4] Gnome through to the end of the list. User should then be able to choose the race by selecting the number and have it stored
def welcome():
        time.sleep(.3)
        print(welcome_message)

def choice_selector(choice_list, list_name):
    print("\nNext up is " +str(list_name)+ " selection.\n")
    time.sleep(1)
    i = 1
    for options in choice_list:
        print("[" + str(i) + "] " + options)
        time.sleep(0.12)
        i += 1
    time.sleep(0.5)
    response = int(input("\nType in the corresponding number for the {} you would like to choose.\n>".format(list_name))) 
    response -= 1
    time.sleep(0.5)
    if response > len(choice_list)-1 or response < 1:
        print("Out of bounds. The highest legit option was " + str(len(choice_list)) + "\n Try again.")
        
        time.sleep(2)
        response = len(choice_list)
        #print("current state of your input is :" + str(response))
        choice_selector(choice_list, list_name)
    print("You have chosen the " + choice_list[response] + " " + str(list_name) + ".")


#def autogen_main():
#
#def auto_or_not():
#    auto_or_not = input("Would you like to do a randomized character?\n[y]\t[n]\n>")
#    if auto_or_not == "y":
#            #autogen_main()
#            print("generating randomized character")
#            auto_or_not()
#    elif auto_or_not != "n":
#            print("Error: incorrect input. Trying again.")
#            auto_or_not()

def main():
    welcome()
    #auto_or_not()
    choice_selector(races, list_name[0])
    choice_selector(class_, list_name[1])
    #choice_selector()
#run the code
main()