import time
from os import system

def sit1(x):
    system("cls")
    print("Feedback: ")
    if x:
        print("\tYou picked the wrong choice.")
        time.sleep(1)
        print("\tUsing harsh malicious words is not a way to communicate.")
        time.sleep(1)
        print("\tYour were just venting out your emotions unilaterally instead.")
        time.sleep(1)
        print("\tEven though your father's words are harsh, insults are still uncalled for.")
        time.sleep(1)
        print("\tAfter all, you are still a family.")
        print("\nRestart the game to explore more!")
    else:
        print("\tWell done!")
        time.sleep(1)
        print("\tYour successfully controlled your anger and attempted to resolve conflicts ironically")
        time.sleep(1)
        print("\tAlthough you haven't been able to completely change his mind,")
        time.sleep(1)
        print("\tyour least success has made him feel that your are trying to discuss with him rationally.")
        time.sleep(1)
        print("\tThat's a good start.")
    print("\n")
    system("pause")


def sit3(x):
    system("cls")
    print("Feedback: ")
    if x == True:
        print("\tYou picked the wrong choice.")

    else:
        print("\tNice job!")
    print("\n")
    system("pause")

def sit5(x):
    system("cls")
    print("Feedback: ")
    if x:
        print("\tYou are too impulsive.")
        time.sleep(1)
        print("\tYour father is obviously a passionate patriot who regards his country as a god.")
        time.sleep(1)
        print("\tYou can't argue against him directly")
        time.sleep(1)
        print("\tWhen you say something bad on the country,")
        time.sleep(1)
        print("\the becomes hostile instantly and that's helpless to persuasion.")
        time.sleep(1)
        print("\tInstead, your should convince them in a gentle way so they don't take it hostile.")
    else:
        print("\tGood")
        time.sleep(1)
        print("\tThe key to lobbying patriotic people is to be more patriotic than them.")
        time.sleep(2)
        print("\tThey cannot refute your motivation.")
        time.sleep(2)
        print("\tAlthough your father might not immediately believe in you,")
        time.sleep(2)
        print("\tthat at least made him feel that you are having similar thoughts.")
        time.sleep(2)
        print("\tThe same argument (conspiracy theory) gave you two a common ground.")

    system("pause")

def sit6(x):
    system("cls")
    print("Feedback: ")
    if x:
        print("\tNot so good...")
        time.sleep(1)
        print("\tScolding your father's friends and questioning their IQ is not the way.")
        time.sleep(2)
        print("\tAdults see their friends as an extension of themselves.")
        time.sleep(2)
        print("\tTeasing their friends is like teasing them.")
        time.sleep(2)
        print("\tTry not the stand on the opposite side of their friends.")
        time.sleep(2)
        print("\tAlso, never force your parents to choose between their children and friends.")
        time.sleep(2)
        print("\tThat triggers the subconscious disgust and force them to seek comfort from friends.")
    else:
        print("\tNot Bad!")
        time.sleep(1)
        print("\tYou tried to involve in the discussion for the sake of your father and his friends.")
        time.sleep(2)
        print("\tYou may not succeed in persuading them to change their stance but at \n\tleast your father felt your kindness.")
        time.sleep(3)
        print("\tYou also forced them to review the information more cautiously.")
        time.sleep(2)
        print("\tHopefully they will be looking at the issues from another angle.")

    system("pause")