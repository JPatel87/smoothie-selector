# Import modules
import time
from termcolor import colored
from recipes import (
    smoothies,
    smoothie_ingrediants
)


def introduction():
    """
    Welcome and introductions, while loop implemented to \
    check user name input; except block executed to handle error \
    if input is not valid. Command line purpose explained.
    """
    print("Welcome to Smoothie Selector!\n")
    time.sleep(2)
    print("Lets start by introducing ourselves,"
          " my name is Coco Nutt.\n")
    time.sleep(2)
    print(colored("What is your name?",
          "yellow"))
    while True:
        try:
            name = input(colored("Enter name\n",
                                 "green")).capitalize()
            if name.isalpha():
                time.sleep(2)
                print(f"\nHello {name}, nice to meet you! Hope you are"
                      " having a great day!\n")
                time.sleep(2)
                print("I am here to help you decide on what smooothie"
                      " to make.\n")
                time.sleep(2)
                print("I will ask you a series of questions and"
                      " then offer you a smoothie suggestion.\n")
                time.sleep(2)
                print("You will have the option to go with my"
                      " suggestion or start again.\n")
                time.sleep(2)
                print("Get yourself a pen and paper, we will be starting"
                      " soon...\n")
                time.sleep(2)
                break
            if not name:
                print("Sorry I didn't catch that...")
                continue
            # Below code inspired from CodeInstitute, love sandwiches project.
            else:
                raise ValueError(f"You entered {name},"
                                 " please enter your name in letters only.")
        except ValueError as e:
            print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))


def countdown():
    """
    Countdown to start smoothie selection process, using import
    time module.
    """
    # Timer code from geeksforgeeks.org
    t = 10
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("**starting in" + " " + timer + " " "seconds**", end="\r")
        time.sleep(1)
        t -= 1


def smoothie_type():
    """
    User is asked to decide what type of smoothie recipe they are interested \
    in; energizing or immunity. while loop implemented to \
    check user input; except block executed to handle error if input is \
    not valid.
    """
    smoothie = smoothies.copy()
    print(colored
          ("Would you like to make an Energizing (E) or Immunity (I)"
           " smoothie?", "yellow"))
    # While loop updates smoothie dictionary based on user input.
    while True:
        type = input(colored("Enter E or I\n",
                             "green")).upper()
        choice_one = "E"
        choice_two = "I"
        if type == choice_one:
            print("\nNice, these types of smoothies are great for"
                  " breakfast or after workouts.\n")
            time.sleep(2)
            print("Logging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Type"] != "E"):
                    smoothie.pop(key1)
            break
        elif type == choice_two:
            print("\nGreat, these types of smoothies"
                  " will keep you going during the flu season.\n")
            time.sleep(2)
            print("Logging your choice...\n")
            # Below code inspired from CodeInstitute, love sandwiches project
            for key1, val1 in list(smoothie.items()):
                if (val1["Type"] != "I"):
                    smoothie.pop(key1)
            break
        else:
            validate_data(type, choice_one, choice_two)

    return smoothie


def validate_data(input, choice_one, choice_two):
    """
    Error handling function, to handle invalid input entries.
    """
    # Code inspired from CodeInstitute, love sandwiches project.
    try:
        if input != choice_one or input != choice_two:
            raise ValueError(f"You entered {input},"
                             f" only {choice_one} or {choice_two}"
                             " entries are valid, please try again.")
    except ValueError as e:
        print(colored(f"Invalid entry: {e}\n", "red", attrs=['bold']))
        return False


def cal(smoothie):
    """
    User is asked to decide whether they are interested \
    in a low calories smoothie. While loop implemented to \
    check user input. Validate data function run to handle error, \
    if input is not valid.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " calories (<200kcal)?", "yellow"))
    # While loop updates smoothie dictionary based on user input.
    while True:
        low_cal = input(colored("Enter Y or N\n", "green")).upper()
        choice_one = "Y"
        choice_two = "N"
        if low_cal == choice_one:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Cal(kcal)"] > 200):
                    smoothie.pop(key1)
            break
        elif low_cal == choice_two:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Cal(kcal)"] < 200):
                    smoothie.pop(key1)
            break
        else:
            validate_data(low_cal, choice_one, choice_two)

    return smoothie


def carbs(smoothie):
    """
    User is asked to decide whether they are interested \
    in a low carbohydrate smoothie. While loop implemented to \
    check user input. Validate data function run to handle error, \
    if input is not valid.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with low"
                  " carbs (<25g)?", "yellow"))
    # While loop updates smoothie dictionary based on user input
    while True:
        low_carbs = input(colored("Enter Y or N\n", "green")).upper()
        choice_one = "Y"
        choice_two = "N"
        if low_carbs == choice_one:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Carbs(g)"] > 25):
                    smoothie.pop(key1)
            break
        elif low_carbs == choice_two:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Carbs(g)"] < 25):
                    smoothie.pop(key1)
            break
        else:
            validate_data(low_carbs, choice_one, choice_two)

    return smoothie


def fruit_veg(smoothie):
    """
    User is asked to decide whether they are interested \
    in a fruit or fruit and veg smoothie. While loop implemented to \
    check user input. Validate data function run to handle error, \
    if input is not valid.
    """
    time.sleep(2)
    print(colored("Would you like to make a smoothie with fruit only (F) or"
                  " fruit and veg (FV)?", "yellow"))
    # While loop updates smoothie dictionary based on user input.
    while True:
        composition = input(colored("Enter F or FV\n", "green")).upper()
        choice_one = "F"
        choice_two = "FV"
        if composition == choice_one:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Ingred"] != "F"):
                    smoothie.pop(key1)
            break
        elif composition == choice_two:
            time.sleep(2)
            print("\nLogging your choice...\n")
            for key1, val1 in list(smoothie.items()):
                if (val1["Ingred"] != "FV"):
                    smoothie.pop(key1)
            break
        else:
            validate_data(composition, choice_one, choice_two)

    return smoothie


def result(smoothie):
    """
    User is shown the smoothie, with calorie, carbohydrate \
    and composition preference data that best fits their \
    responses from previous questions.
    """
    time.sleep(2)
    print("Great, I have a smoothie that ticks all your boxes...\n")
    time.sleep(2)
    for key1, val1 in smoothie.items():
        smoothie_option = key1
        print(colored(f"{key1} smoothie:",
                      "green", "on_yellow", attrs=['bold']))
        print(f'{"Type"} : {val1["Type"]}')
        print(f'{"Cal(kcal)"}/serving : {val1["Cal(kcal)"]}')
        print(f'{"Carbs(g)"}/serving : {val1["Carbs(g)"]}')
        print(f'{"Ingred"} : {val1["Ingred"]}')

    return smoothie_option


def recipe(smoothie_option):
    """
    User is shown the smoothie recipe ingrediants,\
    serving size and method.
    """
    time.sleep(2)
    print("\nHere comes the recipe...\n")
    time.sleep(2)
    for key, values in smoothie_ingrediants.items():
        if key == smoothie_option:
            print(*values, sep='\n')  # code inspired from codegrepper
    print("\nMETHOD:")
    print("1) Wash all fruits and/or vegetables.")
    print("2) Cut any large ingrediants into small cubes.")
    print("3) Whizz everything together in a blender and enjoy!\n")
    time.sleep(4)


def decision():
    """
    User is asked whether they are happy with the suggestion \
    or whether they want to start again.\
    While loop implemented to check user input.\
    Validate data function run to handle error, \
    if input is not valid.
    """
    print(colored("Happy with the selection (H)?"
                  " or would you like to start over (S)?",
                  "yellow"))
    while True:
        decision = input(colored("Enter H or S\n", "green")).upper()
        choice_one = "H"
        choice_two = "S"
        if decision == choice_one:
            time.sleep(2)
            print("\nWonderful, hope you enjoy the smoothie!\n")
            time.sleep(2)
            print("Come and visit again soon!\n")
            time.sleep(2)
            print("Happy blending!")
            break
        elif decision == choice_two:
            time.sleep(2)
            print("\nOk no worries, lets go again...\n")
            time.sleep(2)
            main()
            break
        else:
            validate_data(decision, choice_one, choice_two)


def main():
    """
    Main function to run all functions
    """
    smoothie = smoothie_type()
    cal(smoothie)
    carbs(smoothie)
    fruit_veg(smoothie)
    smoothie_option = result(smoothie)
    recipe(smoothie_option)
    decision()


# Used unicode consortium names for emojis.
print("\U0001F34A" " \U0001F952" " \U0001F34F ", "SMOOTHIE SELECTOR",
      "\U0001F34F" " \U0001F952" " \U0001F34A\n")


introduction()
countdown()
main()
