from os import system
import time, shutil
columns = shutil.get_terminal_size().columns
def Sit2():
    system("cls")
    print("12 November 2019 15:46")
    print("-" * (columns - 23))

    print("Lixkg Notification:")
    print("\tPolice are trying the get into The Chinese University's main campus.")
    time.sleep(1.5)
    print("\tThey are firing tear gases and rubber bullets.")
    time.sleep(2)
    print("\n\tThe protesters are fighting back with molotov cocktails and rocks.")
    time.sleep(2)
    print("\n(You are worried and want to join the protest)")
    print("(You changed and packed everything you need then you met your father by the door)\n")

    choice = "0"
    while (choice != "1" and choice != "2"):
        choice = input("1. Seek permission from father    2. Leave without saying anything (1/2)")

    if choice == "1":
        print("You:\n\tI am going out.")
        time.sleep(2)
        print("Father:\n\tWhere are you going? Are you going to join the rioters?")
        time.sleep(2)
        print("You:\n\tYes, it's like a war zone now.")
        time.sleep(2)
        print("\tI must go and help.")
        time.sleep(2)
        print("Father:\n\tNo! You are not going!")
        time.sleep(2)
        print("\tIt's dangerous! Don't you know it's never easy for a family to gather?!")
        time.sleep(2)
        print("You:\n\tI am 19! I can choose what to do!")
        time.sleep(2)
        print("Father:\n\tNo! It's not gonna happen as long as I am still in the house!")
        time.sleep(2)
        print("\tGet back into your room!")
        time.sleep(3)
        print("\n(With no choice, your are forced to stay in your room)")
        return True
    else:
        print("\t(You said nothing and just went pass your father...)")
        system("pause")
        return False


