from os import system
import time, shutil
columns = shutil.get_terminal_size().columns

def Sit4(): #father realized you left and confronted you
    system("cls")
    print("13 November 2019 09:12")
    print("-" * (columns - 23))

    print("(You get home the next morning and your father was furious...)")
    time.sleep(1)
    print("Father:\n\tWhere have you been all night?\n")

    choice = ""
    while choice != "1" and choice != "2":
        choice = input("1. Lie    2.Truth (1/2)")

    if choice == "1":
        print("\nYou:\n\tI just went to a party with my friends.")
        time.sleep(2)
        print("\tCalm down, I was not in the protest.")
        time.sleep(1)
        print("(You went back to your room and hid the gears.)")
        return True
    else:
        print("\nYou:\n\tI went to the protest.")
        time.sleep(2)
        print("\tThey needed help or my precious college will be sabotaged!")
        time.sleep(2)
        print("\nFather:\n\tYou idiot!")
        time.sleep(1)
        print("\tYou're being used! They are trying to ruin Hong Kong!")
        time.sleep(2)
        print("\tGet back into your room and you are grounded!")
        time.sleep(1)
        print("(He took all your gears and kicked you back into your room)\n")
        return False