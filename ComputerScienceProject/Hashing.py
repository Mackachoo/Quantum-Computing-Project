import string

### This is the class which is an example hashing algorithm.

class HashBot():

    def __init__(self):
        self.item = "Strings. Strings. Everywhere!"
        print("\n\n-=-=-=-=-=-=-=-=-=-= An Example Hashing Algorithm =-=-=-=-=-=-=-=-=-=-")

    ### The initializer function as usual takes the users choice and inputs and hands the off to the other functions in the object.

    def Initialise(self):
        Stay = True
        while Stay:
            try:
                self.item = input("\nEnter text : ")

                print("Do you want to run a hash with working(1) or without working(2) \nor run an unhash with working(3) or without working(4) on this text [To leave enter (0)] :",end=" ")

                choice = int(input())
                if choice == 1:
                    print("Hashed Text :",self.makeHashWorking())
                elif choice == 2:
                    print("Hashed Text :",self.makeHash())
                elif choice == 3:
                    print("Plain Text :",self.undoHashWorking())
                elif choice == 4:
                    print("Plain Text :",self.undoHash())
                elif choice == 0:
                    Stay = False
                else:
                    int("This message will self-destruct now!")
            except:
                print("\nInput Error ---- [Restarting Choice]")
                self.Initialise()

    ### This turns regular plain text into a simple hash.

    def makeHash(self):
        itemList = list(self.item)
        hashList = []
        for i in range(len(itemList)):
            itemNo = string.printable.index(itemList[i])
            hashList.append(itemNo*(i+1))
        print("")
        return " ".join(str(x) for x in hashList)

    ### This is the opposite so turns the hash back into plain text.

    def undoHash(self):
        itemList = []
        hashList = self.item.split()
        for i in range(len(hashList)):
            itemNo = int(hashList[i])
            itemList.append(string.printable[int(itemNo/(i+1))])
        print("")
        return "".join(itemList)

    ### This turns regular plain text into a simple hash, however also shows the working.

    def makeHashWorking(self):
        itemList = list(self.item)
        hashList = []
        for i in range(len(itemList)):
            itemNo = string.printable.index(itemList[i])
            hashList.append(itemNo*(i+1))
            print("\nIn position",i+1,"is",itemList[i],"the ASCII number for this is",itemNo," \n\t\ttherefore the hash number is",i+1,"x",itemNo,"=",str(itemNo*(i+1))+".")
        print("")
        return " ".join(str(x) for x in hashList)

    ### This is the opposite so turns the hash back into plain text, however also shows the working.

    def undoHashWorking(self):
        itemList = []
        hashList = self.item.split()
        for i in range(len(hashList)):
            itemNo = int(hashList[i])
            itemList.append(string.printable[int(itemNo/(i+1))])
            print("\nIn position",i+1,"is",hashList[i],"so to find the ASCII number,",hashList[i],"/",str(i+1)+", this number is equivalent to",string.printable[int(itemNo/(i+1))]+".")
        print("")
        return "".join(itemList)
