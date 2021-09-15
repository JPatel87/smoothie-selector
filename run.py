import time
from recipes import smoothies
from itertools import chain

def introduction():
    """
    Introductions, while loop implemented to check for user name. 
    Project purpose explained.
    """
    print("Welcome to Smoothie Selector!")
    print("Lets start by introducing ourselves, my name is Coco Nutt, Coco for short.")
    while True:
        name = input("What would you like to be called? \n")
        if not name:
            print("Sorry I didn't catch that...")
            continue
        if name:
            time.sleep(1)
            print(f"Hello {name}, nice to meet you! Hope you are having a great day.")
            time.sleep(2)
            print("I am here to help you decide on what smooothie to make today.")
            time.sleep(2)
            print("Get yourself a pen and paper, we will be starting soon...")
            time.sleep(2)
            break

def countdown(t):
    """
    Countdown timer added to start smoothie selection process, using imported time module. 
    """
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("**starting in" + " " + timer + " " "seconds**", end="\r")
        time.sleep(1)
        t -= 1
t = 10   

def smoothie_type_selection():
    """
    User is asked to decide what type of smoothie recipes they are interested in; fruit, fruit and veg or both.
    Used imported chain function from itertools module. 
    """
    print("Would you like to see Fruit(F), Fruit and Veg(FV) or both(B) types of smoothie recipes?") 
    smoothie_select = input("Enter F or FV or B\n")
    if smoothie_select == "F":
        print("Ok so here are our Fruit smoothies...")
        time.sleep(2)
        for smoothie in smoothies["Fruit"]:
            print(smoothie)
    elif smoothie_select == "FV":
        print("Ok, so here are Fruit and Veg smoothies:")
        time.sleep(2)
        for smoothie in smoothies["Fruit_and_Veg"]:
            print(smoothie)
    elif smoothie_select == "B":
        time.sleep(2)
        print("Ok, so here are all our smoothies:")
        for smoothie in chain(smoothies["Fruit"], smoothies["Fruit_and_Veg"]):
            print(smoothie)

introduction()
countdown(t)
smoothie_type_selection()
