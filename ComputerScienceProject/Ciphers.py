import BasicFunctionsLibrary as bfl
import string
import random

### This is the class for the Caesar cipher.

class CaesarBot():

    def __init__(self):
        self.phrase = ""
        self.pushNo = 0

    ### The initializer simply gets the user inputs and choice and sends it to processing.

    def Initialise(self):
        print("\n\n-=-=-=-=-=-=-=-=-=-= The Caesar Cipher =-=-=-=-=-=-=-=-=-=-\n")
        print("This is a very simple cipher which shifts the letters by a certain an to decode only reverse shifting is required.\n")

        Stay = True
        while Stay:
            try:
                choice = input("\nDo you want to encode(1), decode(2)  or crack(3) a message (leave blank to return to main menu) : ")
                if choice == "":
                    Stay = False

                elif choice == "1":
                    self.phrase = input("\nEnter phrase to encode : ")
                    self.pushNo = input("Enter the push number : ")
                    print("""Encoding " """+self.phrase+""" " \n\tpushed by""",self.pushNo+".")
                    print("\nThe enciphered version of this is :",self.EnDeCoder(int(self.pushNo)))
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                elif choice == "2":
                    self.phrase = input("\nEnter phrase to decode : ")
                    self.pushNo = input("Enter the pull number : ")
                    print("""Decoding " """+self.phrase+""" " \n\tpulled by""",self.pushNo+".")
                    print("\nThe deciphered version of this is :",self.EnDeCoder(-int(self.pushNo)))
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                elif choice == "3":
                    self.phrase = input("\nEnter phrase to decode : ")
                    print("Deciphering",self.phrase,":\n")
                    self.GaiusCassiusLonginus()

                else:
                     int("This won't work - ;)")

            except:
                print("\nInput Error ---- [Restarting Choice]")

    ### This function is used to decode text when the key isn't known, it uses frequency and though is relatively simple it is pretty accurate so illustrating the shortcomings of the caesar cipher.

    def GaiusCassiusLonginus(self):
        print("\tAll possible plain versions(in order of likelihood):")
        self.phrase = self.phrase.lower()
        PhraseOptions = []
        LetterFrequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
        for brutus in range(1,26):
            PhraseOptions.append(self.EnDeCoder(-brutus).lower())
        for marcus in range(25):
            TopValueIndex = bfl.HighestOccurrence(PhraseOptions,LetterFrequency[marcus])
            print("\t("+str(marcus+1)+")",PhraseOptions[TopValueIndex])
            del PhraseOptions[TopValueIndex]
        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    ### This is the encoder which is what shifts the plain text, so encoding it. To reverse the same function is used just with a negative shift value.

    def EnDeCoder(self,ppNo):
        List = list(self.phrase)
        for point in range(len(List)):
            try:
                List[point] = string.ascii_letters[(list(string.ascii_letters).index(List[point])+ppNo)%52]
            except:
                pass
        return "".join(List)

### This is the class for the Vigenere cipher.

class VigenereBot():

    def __init__(self):
        self.plainTxt = ""
        self.cipherTxt = ""

    ### The low and high level functions set what characters are available to be encoded and they include just letter characters and all of the ascii characters respectively.

    def LowLevel(self):
        self.unitList = list(string.ascii_letters)
        self.unitList.append(" ")

    def HighLevel(self):
        self.unitList = list(string.printable)

    ### This simply gets the user input for the key or if none is given randomly generates its own depending on the encoding level.

    def GetCipherKey(self):
        if self.cipherTxt == "":
            cipherStore = []
            self.cipherTxt = []
            for i in range(len(self.plainTxt)):
                randIndex = random.randint(0,len(self.unitList)-1)
                self.cipherTxt.append(randIndex)
                cipherStore.append(self.unitList[randIndex])
        else:
            cipherStore = list(self.cipherTxt)[:len(self.plainTxt)]
            self.cipherTxt = []
            for i in range(len(cipherStore)):
                self.cipherTxt.append(self.unitList.index(cipherStore[i]))
        return "".join(cipherStore)

    ### The encoder and decoder are separate in this cipher as the key is stored in character form which doesn't include negatives.

    def Encoder(self,plainTxt,key):
        for point in range(len(plainTxt)):
            try:
                plainTxt[point] = self.unitList[(self.unitList.index(list(plainTxt)[point])+key[point%len(key)])%len(self.unitList)]
            except:
                pass
        return "".join(plainTxt)

    def Decoder(self,cipherTxt,key):
        for point in range(len(cipherTxt)):
            try:
                cipherTxt[point] = self.unitList[(self.unitList.index(list(cipherTxt)[point])-key[point%len(key)])%len(self.unitList)]
            except:
                pass
        return "".join(cipherTxt)

    ### The initializer primary input is how you want to run the program but it also takes the data.

    def Initialise(self):
        print("\n\n-=-=-=-=-=-=-=-=-=-= The Vigenere Cipher =-=-=-=-=-=-=-=-=-=-\n")
        print("This is an incredibly secure cipher particularly if the key is the same length as the pass phrase.\n")

        Stay = True
        while Stay:
            try:
                choiceB = int(input("\nDo you want to encode(1) or decode(2) a message [To leave enter (0)] : "))
                if choiceB == 0:
                    Stay = False
                else:
                    choiceA = input("\n\t~ To start enter the level of encryption : High(1) or Low(2) : ")
                    if choiceA == "1":
                        self.HighLevel()
                    elif choiceA == "2":
                        self.LowLevel()
                    else:
                        int("This won't work")
                    
                    if choiceB == 1:
                        self.plainTxt = input("\nEnter phrase to encode : ")
                        self.cipherTxt = input("Enter the key(leave blank to have one generated) : ")
                        print("""Encoding " """+self.plainTxt+""" " \n\twith key {""",self.GetCipherKey(),"}.")
                        print("\nThe enciphered version of this is :",self.Encoder(list(self.plainTxt),self.cipherTxt))
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    elif choiceB == 2:
                        self.plainTxt = input("\nEnter phrase to decode : ")
                        self.cipherTxt = input("Enter the key(leave blank to have one generated) : ")
                        print("""Decoding " """ + self.plainTxt + """ " \n\twith key""", self.GetCipherKey())
                        print("\nThe deciphered version of this is :", self.Decoder(list(self.plainTxt),self.cipherTxt))
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    else:
                         int("This won't either work - ;)")

            except:
                print("\nInput Error ---- [Restarting Choice]")

### This a secret, shh!

class SecretCipher():

    def __init__(self):
        self.vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
        self.consonants = ['b','B', 'c','C', 'd','D', 'f','F', 'g','G', 'h','H', 'j','J', 'k','K', 'l','L', 'm','M', 'n','N', 'p','P', 'q','Q', 'r','R', 's','S', 't','T', 'v','V', 'w','W', 'x','X', 'z','Z']

    def Initialise(self):
        print("\n\n-=-=-=-=-=-=-=-=-=-= The Language Generator =-=-=-=-=-=-=-=-=-=-")
        print("\nThis is will mix consonants and vowels depending on a specific key")

        self.key = input("\n\t~Enter the language key(leave blank to have one generated) : ")
        print("\t\t~Your key is",self.GetKey())
        self.ConvertAlphabet()

        Stay = True
        while Stay:
            try:
                phrase = str(input("\nPlease enter your phrase to translate(leave empty to return to main menu) : "))
                if phrase == "":
                    Stay = False
                    pass
                else:
                    print(self.Translator(phrase))
            except:
                print("\nInput Error ---- [Restarting Input]\n")
                pass


    def Translator(self,phrase):
        PhraseToList = list(phrase)
        TranslatedPhrase = []
        for current in PhraseToList:
            if current in self.vowels:
                TranslatedPhrase.append(self.ConvertedVowels[self.vowels.index(current)])
            elif current in self.consonants:
                TranslatedPhrase.append(self.ConvertedConsonants[self.consonants.index(current)])
            else:
                TranslatedPhrase.append(current)
        return "".join(TranslatedPhrase)



    def GetKey(self):
        if self.key == "":
            cipherStore = []
            self.key = []
            for i in range(random.randint(1,12)):
                randIndex = random.randint(0,len(string.ascii_letters)-1)
                self.key.append(randIndex)
                cipherStore.append(string.ascii_letters[randIndex])
        else:
            cipherStore = list(self.key)
            self.key = []
            for i in range(len(cipherStore)):
                self.key.append(string.printable.index(cipherStore[i]))
        return "".join(cipherStore)

    def ConvertAlphabet(self):
        self.ConvertedVowels = []
        self.ConvertedConsonants = []

        for indexA in range(len(self.vowels)//2):
            letter = self.vowels[2*((indexA+self.key[indexA%len(self.key)])%6)]
            self.ConvertedVowels.append(letter)
            self.ConvertedVowels.append(letter.upper())

        for indexB in range(len(self.consonants)//2):
            letter = self.consonants[2*((indexB+self.key[indexB%len(self.key)])%20)]
            self.ConvertedConsonants.append(letter)
            self.ConvertedConsonants.append(letter.upper())
