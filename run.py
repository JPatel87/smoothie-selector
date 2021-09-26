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
          "yellow"))
    while True:
        try:
            name = input(colored("Enter name\n",
                                 "green")).capitalize()
            if name.isalpha():
                time.sleep(1)
                print(f"\nHello {name}, nice to meet you! Hope you are having a"
                       " great day!\n")
                time.sleep(2)
                print("I am here to help you decide on what smooothie to make"
                      " today, by asking you a series of questions.\n")
                time.sleep(2)
                print("Get yourself a pen and paper, we will be starting"
                      " soon...\n")
                time.sleep(2)
                break
            if not name:
                print("Sorry I didn't catch that...")
                continue
            else:
                raise ValueError(f"You entered {name},"
                                 " please enter your name in letters only.")
        except ValueError as e:
            print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))


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
    smoothie = smoothies.copy()
    print(colored
          ("Would you like to make an Energizing (E) or Immunity (I)"
           " smoothie?", "yellow"))
    while True:
        type = input(colored("Enter E or I\n",
                             "green")).upper()
        try:
            if type == "E":
                print("Nice choice, these types of smoothies are great for"
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
                raise ValueError(f"You entered {type},"
                                 " only E or I entries are valid, please"
                                 " try again")
        except ValueError as e:
            print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))

    return smoothie


def cal(smoothie):
    """
    User is asked if they would like a low calorie recipe according to which \
    smoothie type they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " calories (<200kcal)?", "yellow"))
    while True:
        low_cal = input(colored("Enter Y or N\n", "green")).upper()
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
                                 " only Y or N entries are valid, please"
                                 " try again")
        except ValueError as e:
            print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))

    return smoothie


def carbs(smoothie):
    """
    User is asked if they would like a low carb recipe according to which \
    calorie level they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " carbs (<25g)?", "yellow"))
    while True:
        low_carbs = input(colored("Enter Y or N\n", "green")).upper()
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
                                 " only Y or N entries are valid, please"
                                 " try again")
        except ValueError as e:
            print(colored(f"Invalid entry: {e} \n", "red", attrs=['bold']))

    return smoothie


def fruit_or_veg(smoothie):
    """
    User is asked if they would like a fruit or fruit and veg recipe \
    according to which carb level they have chosen.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with fruit only (F) or"
                  " fruit and veg (FV)?", "yellow"))
    while True:
        composition = input(colored("Enter F or FV\n", "green")).upper()
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
                                 " only F or FV entries are valid, please"
                                 " try again")
        except ValueError as e:
            print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))

    return smoothie


def result(smoothie):
    print("Great, I have a recipe that ticks all your boxes...\n")
    time.sleep(2)
    for key1, val1 in smoothie.items():
        smoothie_option = key1
        print(colored(f'{key1} smoothie:',
                      "yellow", "on_magenta"))
        print(f'{"Cal(kcal)"}/serving : {val1["Cal(kcal)"]}')
        print(f'{"Carbs(g)"}/serving : {val1["Carbs(g)"]}')
    time.sleep(2)

    return smoothie_option


def decision(smoothie_option):
    print(colored("\nWould you like to see the recipe (R) or start again (S)?",
          "yellow"))
    decision = input(colored("Enter R or S\n", "green")).upper()
    if decision == "S":
        print("Ok no worries, lets go again...\n")
        main()
    if decision == "R":
        print("\nVoila...\n")
        print("To make this smoothie, wash all fruits and vegetables,"
              " cut any large ingrediants into small cubes,"
              " blend and enjoy!\n")
        for key, values in smoothie_ingrediants.items():
            if key == smoothie_option:
                print(colored(f'{key} smoothie:', "yellow",
                              "on_magenta"))
                print(*values, sep='\n')


def main():
    smoothie = smoothie_choice()
    cal(smoothie)
    carbs(smoothie)
    fruit_or_veg(smoothie)
    smoothie_option = result(smoothie)
    decision(smoothie_option)


print("\U0001F34A" " \U0001F952" " \U0001F34F" " Smoothie Selector ",
      "\U0001F34F" " \U0001F952" " \U0001F34A\n")

introduction()
countdown()
main()
