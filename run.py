import time
from recipes import energizing_smoothies
from recipes import immunity_booster_smoothies


def introduction():
    """
    Introductions, while loop implemented to check for user name.
    Project purpose explained.
    """
    print("Welcome to Smoothie Selector!")
    print("Lets start by introducing ourselves, my name is Coco Nutt, \
    Coco for short.")
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
    Countdown timer added to start smoothie selection process, using imported 
    time module.
    """
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("**starting in" + " " + timer + " " "seconds**", end="\r")
        time.sleep(1)
        t -= 1
t = 2

def smoothie_type_selection():
    """
    User is asked to decide what type of smoothie recipe they are interested in; fruit or fruit and veg.
    """
    print("Would you like to make an Energizing smoothie (E) or an Immunity boosting (I) smoothie?") 
    while True:

        try:
            smoothie_select = input("Enter E or I \n").upper()
            if smoothie_select == "E":
                print("Nice choice, these types of smoothies are great for breakfast:")
                time.sleep(2)
                for smoothie in energizing_smoothies:
                    print(smoothie)
                time.sleep(2)
                calories(energizing_smoothies)
                break
            if smoothie_select == "I":
                print("Great choice, these types of smoothies are antioxidant rich too:")
                time.sleep(2)
                for smoothie in immunity_booster_smoothies:
                    print(smoothie)
                calories(immunity_booster_smoothies)
                break
            else:
                raise ValueError(
                f"You entered {smoothie_select}, only E or I values are accepted, please try again"
            )
        except ValueError as e:
            print(f"Invalid data: {e}. \n")

def help_required(str):
    print(str)

def calories(smoothie_type):
    help_required("\nSpoilt for choice, no worries, I'm here to help!\n")
    time.sleep(2)
    print("Would you like to make a smoothie with low calories (<200 kcal)?")
    low_calories = input("Enter Y (yes) or N (not fussed) \n").upper()
    time.sleep(1)
    print("Ok, so here are your choices...")
    time.sleep(2)
    if low_calories == "Y":
        for i in smoothie_type:
            if smoothie_type[i]["Calories per serving (kcal)"] <= 200:
                print(i)

introduction()
countdown(t)
smoothie_type_selection()

