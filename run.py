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
        smooth = input(colored("Enter E or I\n",
                               color="green")).upper()
        try:
            if smooth == "E":
                print("\nNice choice, these types of smoothies are great for"
                      " breakfast or after a long workout.\n")
                time.sleep(2)
                print("Logging your choice...\n")
                time.sleep(2)
                for key1, val1 in list(smoothie.items()):
                    if (val1["Type"] != "E"):
                        smoothie.pop(key1)
                break
            elif smooth == "I":
                print("\nGreat choice, these types of smoothies"
                      " will keep you going during the flu season.\n")
                time.sleep(2)
                print("Logging your choice...\n")
                time.sleep(2)
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
    print(smoothie)


def main():
    introduction()
    countdown()
    smoothie = smoothie_choice()
    cal(smoothie)


print("\U0001F34A" " \U0001F952" " \U0001F34F" " Smoothie Selector",
      "\U0001F34F" " \U0001F952" " \U0001F34A\n")

main()
