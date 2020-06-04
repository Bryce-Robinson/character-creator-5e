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
    #the KEY is the STAT number, the VALUE is the POINTS it cost, max stat in PB is 15.
    tuple_point_buy=(4,-4,5,-3,6,-2,7,-1,8,0,9,1,10,2,11,3,12,4,13,5,14,7,15,9)
    count = 0
    print("Stat values:", end="\t")
    while count < len(tuple_point_buy)-1:
        if count % 2 == 0:
            print(tuple_point_buy[count],end="\t")
        count+=1
    print("\nPoint values:", end="\t")
    count = 0
    while count < len(tuple_point_buy)-1:
        if count % 2 == 1:
            print(tuple_point_buy[count],end="\t")
        count+=1

point_buy(1)