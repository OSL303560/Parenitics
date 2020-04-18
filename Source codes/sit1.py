from os import system
import time, shutil
columns = shutil.get_terminal_size().columns

def Sit1():
# sharing a link in family whatsapp group
    print("12 November 2019 08:50")
    print("-"*(columns-23))
    time.sleep(1)
    print("Whatxapp Group Conversation".center(columns-20))
    time.sleep(1)
    print("12 Nov 2019".center(columns-20) + "\n\tYou:\n\t\thttp://www.lixkg.com/thread/xxxxxx/page/1")
    time.sleep(0.5)
    print("\t\tHong Kong is becoming a sick city with police brutality!")
    time.sleep(2)
    print("\tFather:\n\t\tThat's enough!")
    system("pause")
    system("cls")
# conversation at home
    print("12 November 2019 10:14")
    print("-" * (columns - 23))
    print("Home".center(columns-20))
    time.sleep(1)
    print("Father: (pointing at the TV with TVB on show)")
    print("\tYou childish and naive youngsters are just messing up with our Hong Kong!")
    time.sleep(2)
    print("\tWhen are you gonna stop? Your future is ruined if you get arrested!")
    time.sleep(2)

    choice = "0"
    while (choice != "1" and choice != "2"):
        choice = input("\n1. Strong refute 2. Correct him politely (1/2) ")
    if choice == "1":
        print("\nYou: ")
        print("\tOh so you think it's correct for the police to do whatever they want?")
        time.sleep(2)
        print("\tThey are ignoring the law and beating up adolescents!")
        time.sleep(2)
        print("\tAnd at least the youngsters are brave enough to fight for their goals!")
        time.sleep(2)
        print("\tLook at you. What have you achieved all these years?")
        time.sleep(2)
        print("\tI have to pay for my own college fee!")
        time.sleep(2)
        print("\tSuch a loser. Just go and find your Nana in Tuen Mun Park!")
        time.sleep(2)
        return True
    else:
        print("\nYou:")
        print("\tFather, I am glad that you did care about what's going on.")
        time.sleep(2)
        print("\tBut I don't think that's the real case.")
        time.sleep(2)
        print("\tYes there are people destroying Hong Kong, that's the police and our \"great\" government.")
        time.sleep(2)
        print("\tPlease try watching some other news channels so you can judge wisely.")
        time.sleep(2)
        print("\tWhat you are getting from TVB is not the whole picture.")
        time.sleep(2.5)
        print("\nFather:")
        print("\tReally? Then how do you explain what the mob's doing?")
        time.sleep(2)
        print("\tThey are setting up roadblocks everywhere and now I need to take another route "
              "\n\tto the park for an afternoon walk!")
        time.sleep(2)
        print("\tIt takes like 15 minutes more!")
        time.sleep(2.5)
        print("\nYou:")
        print("\tAre your self interests more important than the future of Hong Kong?")
        time.sleep(2)
        print("\tThe government is trying to take away our freedoms and liberty!")
        time.sleep(2)
        print("\nFather:")
        print("\tSure! I am old enough and the future of Hong Kong no longer matters to me.")
        time.sleep(2)
        print("\tAlso, I understand nothing about politics. \n\tThe only thing I know is that those things are wrong!")
        time.sleep(2)
        print("\nYou:\n\tFine. Whatever you like then.")

        return False