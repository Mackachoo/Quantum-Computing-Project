import Nim as nimGame
import Networks as network
import Ciphers as cipher
import BasicFunctionsLibrary as bfl
import StatisticsCheatSheet as scs
import Matrices as mat
import Hashing as hash

### This is the main class which when you are testing the algorithms runs everything.

class Runner():

    def __init__(self):
        self.choice = 0

    ### This is function that contains the loop which continuously keeps the program running.

    def Start(self):
        self.Welcome()
        while True:
            self.Choose()
            self.RunChoice()

    ### These two functions are primarily text and tell the user all the options and takes their choice as an input.

    def Welcome(self):
        print("\n-=-=-=-=-=-=-=-=-=-= Welcome to the A level Coding Library =-=-=-=-=-=-=-=-=-=-\n\nThis is a library of algorithms of varying complexity which you will most likely\nuse in this course.")
        print("")

    def Choose(self):
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\nPlease choose one of the various algorithms to run/inspect:")
        print("\n-=-=-=-= Easy =-=-=-=-")

        print("(1) The BubbleSort Algorithm")
        print("(2) The Caesar Cipher")

        print("\n-=-=-=- Medium -=-=-=-")

        print("(3) Primm's Algorithm")
        print("(4) Kruskal's Algorithm")
        print("(5) Vigenere Cipher")
        print("(6) Example Hashing Algorithm")
        print("(7) The CycleSort Algorithm")

        print("\n-=-=-=-= Hard =-=-=-=-")

        print("(8) Dijkstra's Algorithm")
        print("(9) The QuickSort Algorithm")
        print("(10) Matrix Operations")
        print("(11) Binomial Recursion")
        print("(12) Recursive Depth Search")

        print("\n-=-=-=- Extras -=-=-=-")

        print("(13) The Nim Game")
        print("(14) Compare Depth Search and Dijkstra's")
        print("(15) Statistics Cheat Sheet")

        print("\n\nTo choose please enter the corresponding index :",end=" ")
        self.choice = input()

    ### This function takes the input from the overarching Start function and then sends the user to the appropriate algorithm.

    def RunChoice(self):
        try:
            if self.choice == "1":
                network.Initialise(self.choice)
            elif self.choice == "2":
                Caesar = cipher.CaesarBot()
                Caesar.Initialise()

            elif self.choice == "3":
                network.Initialise(self.choice)
            elif self.choice == "4":
                network.Initialise(self.choice)
            elif self.choice == "5":
                Vigenere = cipher.VigenereBot()
                Vigenere.Initialise()
            elif self.choice == "6":
                Hasher = hash.HashBot()
                Hasher.Initialise()
            elif self.choice == "7":
                network.Initialise(self.choice)


            elif self.choice == "8":
                network.Initialise(self.choice)
            elif self.choice == "9":
                network.Initialise(self.choice)
            elif self.choice == "10":
                Matrix = mat.MatrixBot()
                Matrix.Initialise()
            elif self.choice == "11":
                bfl.BinomialDistribution()
            elif self.choice == "12":
                network.Initialise(self.choice)

            elif self.choice == "13":
                nimGame.Initialise()
            elif self.choice == "14":
                network.Initialise(self.choice)
            elif self.choice == "15":
                scs.Start()

            elif self.choice == "66":
                Secret = cipher.SecretCipher()
                Secret.Initialise()

            else:
                print("\nInput Error ---- [Restarting]")
                int("爆発!")
        except:
            print("\nError Occurred - [ErrorLoc : Main]")
            pass

### Starts everything!

Alpha = Runner()
Alpha.Start()
