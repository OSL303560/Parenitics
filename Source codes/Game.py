import Beginning, Ending, Propend, Feedbacks, sit1, sit2, sit3, sit4, sit5, sit6
from os import system
relev = 1 #relationship level, Not showing in game but it decides which ending the game reaches
def main():
    global relev
    Beginning.introduction()
    Beginning.startstory()

    if sit1.Sit1(): #picking the wrong choice in situation 1 - gameover
        Ending.Gameover_1()
        system("pause")
        Feedbacks.sit1(True)
        exit()
    else: #picking the right choice in situation 1 - game continues & better relationship
        system("pause")
        Feedbacks.sit1(False)
        relev += 1

    if sit2.Sit2(): #picking choice 1 in situation 2 - goes into situation 3
        if sit3.Sit3(): #picking wrong choice in situation 3 - gameover
            Ending.Gameover_2()
            system("pause")
            Feedbacks.sit3(True)
            system("pause")
            Propend.out()
        else: #picking the right choice in situation 3 - game continues & better relationship
            relev += 1
            system("pause")

    else:#picking choice 2 in situation 2 - goes into situation 4
        if sit4.Sit4() == False:
            relev -= 1
        system("pause")

    if sit5.Sit5():#picking choice 1 in situation 5
        Feedbacks.sit5(True)
    else:
        Feedbacks.sit5(False)#picking choice 2 in situation 5 - better relationship
        relev += 1

    if sit6.Sit6():#picking choice 1 in situation 6 - worse relationship
        Feedbacks.sit6(True)
        relev -= 1
    else:#picking choice 2 in situation 5 - better relationship
        Feedbacks.sit6(False)
        relev += 1
    Propend.out()#end of prototype


main()