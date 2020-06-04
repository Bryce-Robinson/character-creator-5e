PYTHONDONTWRITEBYTECODE=" "
import random
#---------------------STAT ROLL SYSTEMS-----------------------------
def three_d_six_strict():
    pass 

def three_d_six_three_times_use_highest():
    pass

def four_d_six_drop_lowest():
    pass

def four_d_six_drop_lowest_reroll_ones():
    pass

def point_buy(point_amount=25):
    def display_point_buy_data():
        #the KEY is the STAT number, the VALUE is the POINTS it cost, max stat in PB is 15.
        point_buy_tuple=(4,-4,5,-3,6,-2,7,-1,8,0,9,1,10,2,11,3,12,4,13,5,14,7,15,9)
        count = 0
        print("Stat values:", end="\t")
        while count < len(point_buy_tuple):
            if count % 2 == 0:
                print(point_buy_tuple[count],end="\t")
            count+=1
        print("\nPoint values:", end="\t")
        count = 0
        while count < len(point_buy_tuple):
            if count % 2 == 1:
                print(point_buy_tuple[count],end="\t")
            count+=1
    def assign_stats_to_character():
        stats_not_assigned = "StrDexConIntWisCha"
        while stats_not_assigned is not "":
            query = input("What would you like to assign to {name}?, type the stat abbreviation followed by the number.\nHere are the stats left to assign followed by points left: {stats_not_assigned}, {points_left} e.g. Dex 10.").format()
            
    display_point_buy_data()
point_buy(1)