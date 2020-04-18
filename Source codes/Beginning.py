import time
from os import system
temp = 0
def startstory():
    print("In February 2019, ", end = "")
    time.sleep(1)
    print("the Hong Kong government proposed the ")
    time.sleep(0.5)
    print("\nFugitive Offenders and Mutual legal Assistance in Criminal Matters Legislation (Amendment) Bill 2019.")
    time.sleep(2)
    print("\nThe bill raised concerns and triggered series of protests.")
    time.sleep(2)
    print("\nThe main movement started in June 2019 and Hong Kong was rocked by protests.")
    time.sleep(2)
    print("\nCarrie Lam, the chief executive, announced the withdrawal of the bill on "
          "4th September but the protests did not stop.")
    time.sleep(2)
    print("\nFocus changed to the police brutality and indiscriminate arrests during previous protests.")
    time.sleep(2)
    print("\nProtesters were demanding full democracy rights for HongKongers and there was no sign of dying down.")
    time.sleep(2)
    print("\nThe message was crystal clear: protests will continue until the five demands are met...\n")
    system("pause")

    system("cls")
    time.sleep(0.5)

def introduction():
    print("Welcome!")
    time.sleep(1)
    print("\nIn this game, you will experience what it's like to be a Hongkonger "
          "\ncommunicating with his parents with opposing political views.")
    time.sleep(1)
    print("\nThe rules are simple. You lose if you pick the wrong choice.")
    time.sleep(1)
    print("\n(This story is fictitious. Any resemblance to actual events are entirely coincidental.)")
    print("(The production team takes no political stance.)\n")
    time.sleep(1)
    answer = "o"

    while answer.lower().strip() != "yes" and answer.lower().strip() != "no":
        answer = input("Understand and Continue? (yes/no)")
    system("cls")

    if answer.lower().strip() == "yes":
        pass
    else:
        print("That's so bad. Goodbye then.")
        exit()