from os import system
import time, shutil
columns = shutil.get_terminal_size().columns

def Sit6():
    system("cls")
    print("13 November 2019 19:26")
    print("-" * (columns - 23))
    print("home".center(columns-20))
    print("(Your father thinks your thoughts are wrong and distorted)")
    print("(He tries to correct you by showing you photos from his friends)")
    time.sleep(2)
    print("\nFather:\n\tSee, these photos are the evidence proofing that the protesters are manipulated!")
    print("\t(Showing photos foreign \"CIA\" talking to protesters)\n")
    time.sleep(2)
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("1. Aggressive   2. Ask to join the group chat (1/2)")

    if choice == "1":
        print("\nYou:\n\tYour uneducated friends with low IQ sent you those pics?")
        time.sleep(2)
        print("\tThey are just trying to brainwash you!")
        time.sleep(2)
        print("\tHow stupid are you to actually believe in those fair weather friends?")
        time.sleep(3)
        print("\nFather:\n\tI have known them for many years! ")
        time.sleep(1.5)
        print("\tThey are not gonna deceive me!")
        time.sleep(2)
        print("\tDo you even know the word \"respect\"?")
        time.sleep(2)
        print("\nYou:\n\tOkay pick one then. Who are you gonna trust?")
        time.sleep(2)
        print("\tYour son or your friends?")
        time.sleep(2)
        print("\nFather:\n\tI am not talking to you anymore!")
        time.sleep(2)
        print("\tSuch an idiot!")
        print("(Slammed and locked his room's door)\n")
        system("pause")
        return True
    else:
        print("\nYou:\n\tOh really? I am surprised that your friends actually received these amazing news!")
        time.sleep(2)
        print("\tBut I am worried that your friends might be fooled by content farms.")
        time.sleep(2)
        print("\tMay I join your group chat and discuss about that?")
        time.sleep(2)
        print("\nFather:\n\tSure! I don't see why not!")
        time.sleep(2)
        print("\n(You installed WeChat on your phone and joined the group chat..)")
        print("(Then sent a few fact checked articles about the CIA issue from the facebook page \"Kauyimmedia\"(求驗傳媒))")
        time.sleep(4)
        print("\nFather:\n\tHey! What are you doing!?")
        time.sleep(2)
        print("\nYou:\n\tI am just worried about your friends being deceived by unreliable websites.")
        time.sleep(2)
        print("\tTrust me! If your friends really do embrace the truth,")
        time.sleep(1.5)
        print("\tthey are definitely gonna like what I sent them.")
        time.sleep(2)
        print("\n(As a result, you had a great debate with the group members)")
        print("(And you noticed that father showed a tiny bit of uncertainty of his beloved faith")
        system("pause")
        return False

