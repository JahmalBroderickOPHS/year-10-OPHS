def player1game():
    print("1 player1 game chosen")
def player2game():
    print(" player2 game chosen")

def online():
    print("online game chosen")
    
def menu():
    print("press 1 for 1 player game")
    print("press 2 for 2 player game")
    print("press 3 for online")
    print("press 4 to exit")

    userInput = int(input("Enter 1, 2, 3 or 4"))

    if userInput == 1:
        player1game()
    elif userInput == 2:
        player2game()
    elif userInput == 3:
        online
    elif userInput == 4:
        print("Exiting....")
    else:
        print("")
        print("input invalid")
        menu()





menu()
