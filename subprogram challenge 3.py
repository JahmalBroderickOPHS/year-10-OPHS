def oneplayer():
    print("")
    print("1-player slected")
    print("")
    
def twoplayer():
    print("")
    print("2-player selected")
    print("")
    
def online():
    print("")
    print("online selected")
    print("")
    
def exiting():
    print("")
    print("exiting...")
    print("")
    
def menu():
    print("")
    print("press (1) for 1-player")
    print("press (2) for 2-player")
    print("press (3) for online")
    print("press (4) to exit")
    print("")




        
menu()

userInput = int(input("please enter your option>>> "))

if userInput == 1:
        oneplayer()
elif userInput == 2: 
        twoplayer()
elif userInput == 3:
       online()
elif userInput == 4:
        exiting()


            
            
