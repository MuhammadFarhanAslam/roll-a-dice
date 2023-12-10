import random

goodbye = "Ok! See you soon"
continue_playing = True

while continue_playing:
    initial_query = "\nDo you want to roll a dice? (y/yes or n/no)\n"
    response = input(initial_query).lower()

    if response == "y" or response == "yes":
        num = random.randint(1, 6)
        if num == 1:
            print("[---]\n[---]\n[ 0 ]\n[---]\n[---]")
        elif num == 2:
            print("[---]\n[ 0 ]\n[---]\n[ 0 ]\n[---]")
        elif num == 3:
            print("[---]\n[ 0 ]\n[ 0 ]\n[ 0 ]\n[---]")
        elif num == 4:
            print("[---]\n[0 0]\n[---]\n[0 0]\n[---]")
        elif num == 5:
            print("[---]\n[0 0]\n[ 0 ]\n[0 0]\n[---]")
        else:
            print("[---]\n[0 0]\n[0 0]\n[0 0]\n[---]")

        continue_query = "\nDo you want to continue? (y/yes or n/no)\n"
        post_roll = input(continue_query).lower()
        if post_roll == "n" or post_roll == "no":
            print(goodbye)
            continue_playing = False

    elif response == "n" or response == "no":
        print(goodbye)
        continue_playing = False

    else:
        print("Invalid response. Please enter 'y' or 'n'.")
