import time

def introduction():
    """Introductions, while loop implemented to check for user name. 
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
            time.sleep(2)
            print(f"Hello {name}, nice to meet you! Hope you are having a great day.")
            time.sleep(2)
            print("I am here to help you decide on what smooothie to make today.")
            time.sleep(3)
            print("Get yourself a pen and paper, we will be starting in...")
            time.sleep(3)
            break

def countdown(t):
    """Countdown timer added to start smoothie selection process, using imported time module. 
    """
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer + " " "seconds", end="\r")
        time.sleep(1)
        t -= 1
t = 10   

introduction()
countdown(t)
