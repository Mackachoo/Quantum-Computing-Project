import random

### This class is for the stack.

class Pile():

    def __init__(self,currentValue):
        self.currentValue = currentValue

    def removeAmount(self,removeAmount):
        self.currentValue = self.currentValue - removeAmount

### This class is for the AI.

class AIPlayer():

    def __init__(self,aiName,currentChoice):
        self.aiName = aiName
        self.currentChoice = currentChoice

    ### This function returns the AI choice on medium difficulty, it returns a 3:1 random mix of the hard and the easy choices.

    def MakeChoiceMed(self,TheStack):
        RandMed = random.randint(0,100)

        if RandMed < 100-(3*TheStack.currentValue):
            self.currentChoice = self.MakeChoiceEasy()
        else:
            self.currentChoice = self.MakeChoiceHard(TheStack)

        return self.currentChoice

    ### This function returns the AI choice on easy difficulty, it returns a random choice.

    def MakeChoiceEasy(self):
        self.currentChoice = random.randint(1,3)
        return self.currentChoice

    ### This function returns the AI choice on hard difficulty, it uses the maths of the game to calculate the perfect answer and will always work providing the stack doesn't start as 4n + 1.

    def MakeChoiceHard(self,TheStack):
        choiceRing = [3,random.randint(1,3),1,2]
        choiceCalc = TheStack.currentValue % 4

        self.currentChoice = choiceRing[choiceCalc]
        return self.currentChoice

### This is the class for the player.

class HumanPlayer():

    def __init__(self,playerName,currentChoice):
        self.PlayerName = playerName
        self.currentChoice = currentChoice

    ### This function only gets the users choice and returns it.

    def MakeChoice(self):
        NotDone = True
        while NotDone:
            print(self.PlayerName,"make your choice(1-3) : ")
            self.currentChoice = int(input())

            if self.currentChoice >= 1 and self.currentChoice <= 3:
                NotDone = False

        return self.currentChoice

### This is the function that runs the game.

def GameStart(GameType,TheStack):

    ### This runs the game with two players.

    if GameType == 1:
        aName = input("\nPlayer 1 choose name : ")
        bName = input("Player 2 choose name : ")
        PlayerA = HumanPlayer(aName,0)
        PlayerB = HumanPlayer(bName,0)
        RUN = True

        while RUN:

            if RUN:
                print("\nThe current value is",TheStack.currentValue)
                TheStack.removeAmount(PlayerA.MakeChoice())

                if TheStack.currentValue <= 0:
                    WhoLose = PlayerA.PlayerName
                    RUN = False

            if RUN:
                print("\nThe current value is",TheStack.currentValue)
                TheStack.removeAmount(PlayerB.MakeChoice())

                if TheStack.currentValue <= 0:
                    WhoLose = PlayerB.PlayerName
                    RUN = False

    ### This runs the game with a player and an AI.

    elif GameType >= 2:
        if  GameType == 5:                                  # Sets the stack for impossible to be unbeatable (removes the possibility of it ever being 4n + 1). #
            List = [16,18,19,20,22,23,24]
            TheStack.currentValue = List[random.randint(0,2)]
        Name = input("\nPlayer choose name : ")
        Player = HumanPlayer(Name,0)
        aiPlayer = AIPlayer("NimBot",0)

        RUN = True

        while RUN:

            if RUN:
                print("\nThe current value is",TheStack.currentValue)
                TempStore = TheStack.currentValue

                if GameType == 2:                                       # This is where the difficulty is decided #
                    TheStack.removeAmount(aiPlayer.MakeChoiceEasy())
                elif GameType == 3:
                    TheStack.removeAmount(aiPlayer.MakeChoiceMed(TheStack))
                elif GameType == 4 or GameType == 5:
                    TheStack.removeAmount(aiPlayer.MakeChoiceHard(TheStack))
                else:
                    print("Error : Code 1")

                print(aiPlayer.aiName,"chose",TempStore-TheStack.currentValue)

                if TheStack.currentValue <= 0:
                    WhoLose = aiPlayer.aiName
                    RUN = False

            if RUN:
                print("\nThe current value is",TheStack.currentValue)
                TheStack.removeAmount(Player.MakeChoice())

                if TheStack.currentValue <= 0:
                    WhoLose = Player.PlayerName
                    RUN = False

    print(WhoLose,"loses!")

### This gets the user input for the game type and then runs the appropriate type.

def Initialise():
    print("\n\n-=-=-=-=-=-=-=-=-=-= Welcome to Nim =-=-=-=-=-=-=-=-=-=-\n\n")
    print("The game is too force your opposition to be the one to make \nzero by choosing the correct numbers.")

    print("\nTo start, please choose gamemode :")
    print("\n     (1) Player vs Player")
    print("     (2) Player vs Computer[Easy]")
    print("     (3) Player vs Computer[Medium]")
    print("     (4) Player vs Computer[Hard]")
    print("     (5) Player vs Computer[Impossible]")
    print("\n     (0) Choose a different algorithm")

    try:
        print("\n\nTo choose please enter the corresponding index :",end=" ")
        choice = input()

        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            TheStack = Pile(random.randint(15,25))
            GameStart(int(choice),TheStack)
        elif choice == "0":
            pass
        else:
            int("This better break ;)")

    except:
        print("\nInput Error ---- [Restarting Nim]")
        Initialise()
