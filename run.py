import time
from termcolor import colored
from recipes import (
    smoothies,
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


def smoothie_choice():
    """
    User is asked to decide what type of smoothie recipe they are interested \
    in; energizing or immunity, if they do not answer correctly an error \
    message will appear and they will be asked to re-enter their choice.
    """
    smoothie = smoothies
    print(colored
          ("Would you like to make an Energizing(E) or Immunity(I) smoothie?",
           color="yellow", on_color="on_red"))
    while True:
        type = input(colored("Enter E or I\n",
                               color="green")).upper()
        try:
            if type == "E":
                print("\nNice choice, these types of smoothies are great for"
                      " breakfast or after a long workout.\n")
                time.sleep(2)
                print("Logging your choice...\n")
                for key1, val1 in list(smoothie.items()):
                    if (val1["Type"] != "E"):
                        smoothie.pop(key1)
                break
            elif type == "I":
                print("\nGreat choice, these types of smoothies"
                      " will keep you going during the flu season.\n")
                print("Logging your choice...\n")
                time.sleep(1)
                for key1, val1 in list(smoothie.items()):
                    if (val1["Type"] != "I"):
                        smoothie.pop(key1)
                break
            else:
                raise ValueError(f"You entered {smooth},"
                                 " only E or I values are accepted, please"
                                 " try again")
        except ValueError as e:
            print(f"Invalid data: {e}. \n")

    return smoothie


def cal(smoothie):
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
                time.sleep(2)
                print("\nLogging your choice...\n")
                for key1, val1 in list(smoothie.items()):
                    if (val1["Cal(kcal)"] > 200):
                        smoothie.pop(key1)
                break
            elif low_cal == "N":
                time.sleep(2)
                print("\nLogging your choice...\n")
                for key1, val1 in list(smoothie.items()):
                    if (val1["Cal(kcal)"] < 200):
                        smoothie.pop(key1)
                break
            else:
                raise ValueError(f"You entered {low_cal},"
                                 " only Y or N values are accepted, please"
                                 " try again")
        except ValueError as e:
            print(f"Invalid data: {e}. \n")

    return smoothie


def carbs(smoothie):
    """
    User is asked if they would like a low carb recipe according to which \
    calorie level they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " carbs (<25 g)?", color="yellow", on_color="on_red"))
    time.sleep(2)
    while True:
        low_carbs = input(colored("Enter Y or N\n", color="green")).upper()
        try:
            if low_carbs == "Y":
                time.sleep(2)
                print("\nLogging your choice...\n")
                for key1, val1 in list(smoothie.items()):
                    if (val1["Carbs(g)"] > 25):
                        smoothie.pop(key1)
                break
            elif low_carbs == "N":
                time.sleep(2)
                print("\nLogging your choice...\n")
                for key1, val1 in list(smoothie.items()):
                    if (val1["Carbs(g)"] < 25):
                        smoothie.pop(key1)
                break
            else:
                raise ValueError(f"You entered {low_carbs},"
                                 " only Y or N values are accepted, please"
                                 " try again")
        except ValueError as e:
            print(f"Invalid data: {e}. \n")

    return smoothie


def fruit_or_veg(smoothie):
    """
    User is asked if they would like a fruit or fruit and veg recipe according \
    to which carb level they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with fruit only (F) or"
                  " fruit and veg (FV)?", color="yellow", on_color="on_red"))
    time.sleep(2)
    while True:
        composition = input(colored("Enter F or FV\n", color="green")).upper()
        try:
            if composition == "F":
                time.sleep(2)
                print("\nLogging your choice...\n")
                time.sleep(1)
                for key1, val1 in list(smoothie.items()):
                    if (val1["Ingred"] != "F"):
                        smoothie.pop(key1)
                break
            elif composition == "FV":
                time.sleep(1)
                print("\nLogging your choice...\n")
                time.sleep(2)
                for key1, val1 in list(smoothie.items()):
                    if (val1["Ingred"] != "FV"):
                        smoothie.pop(key1)
                break
            else:
                raise ValueError(f"You entered {composition},"
                                 " only Y or N values are accepted, please"
                                 " try again")
        except ValueError as e:
            print(f"Invalid data: {e}. \n")

    return smoothie


def result(smoothie):
    print(smoothie)


def main():
    introduction()
    countdown()
    smoothie = smoothie_choice()
    cal(smoothie)
    carbs(smoothie)
    fruit_or_veg(smoothie)
    result(smoothie)


print("\U0001F34A" " \U0001F952" " \U0001F34F" " Smoothie Selector",
      "\U0001F34F" " \U0001F952" " \U0001F34A\n")

main()
