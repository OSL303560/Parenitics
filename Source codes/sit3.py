from os import system
import time, shutil
columns = shutil.get_terminal_size().columns

def Sit3():
    print("(However, you have another idea when things get worse...)")

    print("12 November 2019 16:18")
    print("-" * (columns - 23))
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("1. Sneak out when father is sleeping    2. Stay home (1/2)")

    if choice == "1":
        print("(You discovered you father is bathing and you left home secretly...")
        time.sleep(1)
        return True
    else:
        print("(You decided to wait for another chance to explain why you eager to go out)\n")
        return False