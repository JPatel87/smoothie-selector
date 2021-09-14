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
            print(f"Hello {name}, nice to meet you! Hope your having a great day")
            print("I am here to help you decide on what smooothie to make today, so without further ado lets make a start!")
            break
            
introduction()
