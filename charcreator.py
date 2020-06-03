import random, time, classes
#lists
list_name = ["race", "class"]
races = ["Human", "Elf", "Dwarf", "Gnome", "Halfling", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling"]
class_ = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
sub_cleric = []
sub_fighter = []


#variables
welcome_message = "Welcome to the Dungeon's and Dragons Command-line Character Generator!\nFor the sake of simplicity and realistic common characters this program will only be using content from the Players Handbook. \nIf you want to create specific characters from the other expansions then you will have to use something else."





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
        time.sleep(0.08)
        i += 1
    time.sleep(0.5)
    res = int(input("\nType in the corresponding number for the {} you would like to choose.\n>".format(list_name)))
    time.sleep(0.5)
    x = res - 1 
    print("Successfully converted to integer form. You have chosen the " + choice_list[x] + " " + str(list_name) + ".")


#def autogen_main():

def auto_or_not():
    auto_or_not = input("Would you like to do a randomized character?\n[y]\t[n]\n>")
    if auto_or_not == "y":
            #autogen_main()
            print("generating randomized character")
            auto_or_not()
    elif auto_or_not != "n":
            print("Error: incorrect input. Trying again.")
            auto_or_not()

def main():
    welcome()
    #auto_or_not()
    choice_selector(races, list_name[0])
    choice_selector(class_, list_name[1])
    #choice_selector()
#run the code
main()