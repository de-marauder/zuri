import random


def rps():
    # Rock paper scissors game.

    options = ["r", "p", "s"]

    print("*"*100)
    username = input(
        "********  Welcome traveller!  ******** \nWhat would you like to be called: ")
    print("*"*100)
    print("\n")
    print("*"*100)
    print("This is a game of rock paper scissors. \nI reckon you've heard of it.")
    print("Today you shall battle me!")
    print("Winner takes all. \nMay our sparring be glorious!")
    print("*"*100)
    print("\n")

    game = True

    while game:
        choice = input(
            f"{username.capitalize()} please enter 'r' for rock, 'p' for paper and 's' for scissors:\n")
        print(f"{username.capitalize()} selects: {choice}\n")
        if choice.lower() not in options:
            print(f"{username.capitalize()} please select a valid option from the choices given.\n")
            continue
        my_choice = random.choice(options)
        print(f"CPU selects: {my_choice}\n")


        if choice.lower() == my_choice.lower():
            print(f"Aha! {username.capitalize()} we seem to be at an impasse. lets try again shall we!\n")
            continue
        # conditons for CPU winning
        elif (choice.lower() == 'r') and (my_choice.lower() == 'p'):
            print("Better luck next time. I have won this round!\n")
            game = False
        elif (choice.lower() == 's') and (my_choice.lower() == 'r'):
            print("Better luck next time. I have won this round!\n")
            game = False
        elif (choice.lower() == 'p') and (my_choice.lower() == 's'):
            print("Better luck next time. I have won this round!\n")
            game = False

        # If cpu can't win then the only option left is player wins.
        else: 
            print(f"{username} wins")
            print(f"You're indeed a strong one {username} for mere mortals seldom best me! \nYou have my respect.\n")
            game = False
        
    return


rps()