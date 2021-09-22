import time
from termcolor import colored
from recipes import (
    energizing_smoothies,
    immunity_smoothies,
    smoothie_ingrediants
)


def introduction():
    """
    Introductions, while loop implemented to check for user name.
    Project purpose explained.
    """
    print("Welcome, lets start by introducing ourselves,",
          "my name is Coco Nutt, Coco for short.\n")
    print(colored("What would you like to be called?",
          color="yellow", on_color="on_red"))
    while True:
        name = input(colored("Enter name\n", color="green"))
        if not name:
            print("Sorry I didn't catch that...")
            continue
        if name:
            time.sleep(1)
            print(f"\nHello {name}, nice to meet you! Hope you are having a"
                  " great day.\n")
            time.sleep(2)
            print("I am here to help you decide on what smooothie to make"
                  " today.\n")
            time.sleep(2)
            print("Get yourself a pen and paper, we will be starting soon...\n")
            time.sleep(2)
            break


def countdown():
    """
    Countdown timer added to start smoothie selection process, using imported
    time module.
    """
    t = 2
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("**starting in" + " " + timer + " " "seconds**", end="\r")
        time.sleep(1)
        t -= 1


def smoothie_type_selection():
    """
    User is asked to decide what type of smoothie recipe they are interested \
    in; fruit or fruit and veg.
    """
    print(colored
          ("Would you like to make an Energizing(E) or Immunity(I) smoothie?",
           color="yellow", on_color="on_red")
          )
    while True:
        smoothie_type = input(colored("Enter E or I\n",
                                      color="green")).upper()
        try:
            if smoothie_type == "E":
                print("\nNice choice, these types of smoothies are great for"
                      " breakfast or after a long workout.\n")
                time.sleep(2)
                print("Logging your choice...\n")
                time.sleep(2)
                calories(energizing_smoothies)
                break
            if smoothie_type == "I":
                print("\nGreat choice, these types of smoothies"
                      " will keep you going during the flu season\n")
                time.sleep(2)
                print("Logging your choice...\n")
                time.sleep(2)
                calories(immunity_smoothies)
                break
            else:
                raise ValueError(f"You entered {smoothie_type},"
                                 " only E or I values are accepted, please"
                                 " try again")
        except ValueError as e:
            print(f"Invalid data: {e}. \n")


def calories(smoothie_type):
    """
    User is asked if they would like a low calorie recipe according to which \
    smoothie type they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " calories (<200 kcal)?", color="yellow", on_color="on_red"))
    time.sleep(2)
    while True:
        low_cal = input(colored("Enter Y or N\n", color="green")).upper()
        try:
            if low_cal == "Y":
                print("\nLogging your choice...\n")
                carbs(low_cal, smoothie_type)
                break
            if low_cal == "N":
                print("\nLogging your choice...\n")
                carbs(low_cal, smoothie_type)
                break
            else:
                raise ValueError(f"You entered {low_cal}, only Y or N values"
                                 " are accepted, please try again")
        except ValueError as e:
            print(f"Invalid data: {e}.\n")


def carbs(low_cal, smoothie_type):
    """
    User is asked if they would like a low carbs recipe according to which \
    smoothie type and calorie option they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low carbs (<25g)?",
                  color="yellow", on_color="on_red"))
    time.sleep(2)
    while True:
        low_carbs = input(colored("Enter Y or N\n", color="green")).upper()
        smoothie_options = []
        try:
            if low_cal == "Y" and low_carbs == "Y":
                print("\nLogging your choice...\n")
                time.sleep(2)
                for i in smoothie_type:
                    if smoothie_type[i]["Cal(kcal)"] <= 200 and smoothie_type[i]["Carbs(g)"] < 25:
                        smoothie_options.append(i)
                decision(smoothie_options)
                break
            if low_cal == "N" and low_carbs == "N":
                print("\nLogging your choice...\n")
                time.sleep(2)
                for i in smoothie_type:
                    if smoothie_type[i]["Cal(kcal)"] > 200 and smoothie_type[i]["Carbs(g)"] >= 25:
                        smoothie_options.append(i)
                decision(smoothie_options)     
                break
            if low_cal == "N" and low_carbs == "Y":
                print("\nLogging your choice...\n")
                time.sleep(2)
                for i in smoothie_type:
                    if smoothie_type[i]["Cal(kcal)"] > 200 and smoothie_type[i]["Carbs(g)"] < 25:
                        smoothie_options.append(i)    
                decision(smoothie_options)   
                break
            if low_cal == "Y" and low_carbs == "N":
                print("\nLogging your choice...\n")
                time.sleep(2)
                for i in smoothie_type:
                    if smoothie_type[i]["Cal(kcal)"] <= 200 and smoothie_type[i]["Carbs(g)"] >= 25:
                        smoothie_options.append(i)
                decision(smoothie_options)
                break
            else:
                raise ValueError(f"You entered {low_carbs}, only Y or N values"
                                 "are accepted, please try again")
        except ValueError as e:
            print(f"Invalid data: {e}.\n")


def decision(smoothie_options):
    for smoothie in smoothie_options:
        print(smoothie)


print("\U0001F34A" " \U0001F952" " \U0001F34F" " Smoothie Selector",
      "\U0001F34F" " \U0001F952" " \U0001F34A\n")


introduction()
countdown()
smoothie_type_selection()