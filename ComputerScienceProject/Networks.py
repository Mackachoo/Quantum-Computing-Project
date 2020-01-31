import Sorting as sort
import BasicFunctionsLibrary as bfl
import SpanningTree as st
import Hashing as hash
import time

### This is a secondary function for running which starts all the algorithms which use the class NetworkBot, it's called directly from Main.

def Initialise(choice):
    ClassBotAlpha = NetworkBot()
    if choice == "1":
        print("\n\n-=-=-=-=-=-=-=-=-=-= The BubbleSort Algorithm =-=-=-=-=-=-=-=-=-=-\n")
        print(sort.BubbleBot(ClassBotAlpha.MakeList()))
    elif choice == "3":
        Matrix, NodeNames = ClassBotAlpha.MakeNetwork()
        Primms = st.PrimmBot(Matrix,NodeNames)
        Primms.Initialise()
    elif choice == "4":
        Matrix, NodeNames = ClassBotAlpha.MakeNetwork()
        Kruskal = st.KruskalBot(Matrix,NodeNames)
        Kruskal.Initialise()
    elif choice == "7":
        print("\n\n-=-=-=-=-=-=-=-=-=-= The CycleSort Algorithm =-=-=-=-=-=-=-=-=-=-\n")
        CycleSortBot = sort.CycleBot(ClassBotAlpha.MakeList())
        print("Sorted list:",CycleSortBot.Initialise())
    elif choice == "8":
        Dijkstra = DijkstraBot(0,0)
        Dijkstra.Initialise()
    elif choice == "9":
        print("\n\n-=-=-=-=-=-=-=-=-=-= The QuickSort Algorithm =-=-=-=-=-=-=-=-=-=-\n")
        QuickSortBot = sort.QuickBot(ClassBotAlpha.MakeList())
        print("\nSorted list:",QuickSortBot.Initialise())
    elif choice == "12":
        DepthSearch = DepthBot(0,0)
        DepthSearch.Initialise()
    elif choice == "14":
        Matrix, NodeNames = ClassBotAlpha.MakeNetwork()
        OverFunc = ShortestPathBot(Matrix, NodeNames)
        start, end = OverFunc.Input()
        timeDi = DijkstraBot(Matrix, NodeNames)
        timeDe = DepthBot(Matrix, NodeNames)
        timeDi.Timer(start,end)
        timeDe.Timer(start,end)

    else:
        print("\nError Occurred ---- [ErrorLoc : Networks]")

### This is a binary search algorithm.

def BinarySearch(List,Target):
    quick = sort.QuickBot(List)
    orderedList = quick.Initialise()
    center = (len(orderedList)+1)//2
    if Target == orderedList[center]:
        return True
    elif len(orderedList) <= 2:
        return False
    elif Target > orderedList[center]:
        return BinarySearch(orderedList[len(orderedList)//2:],Target)
    elif Target < orderedList[center]:
        return BinarySearch(orderedList[:len(orderedList)//2],Target)

### This is the class which primarily does the Network handling but also the list handling.

class NetworkBot():

    def __init__(self):
        pass

    ### This is the function that gets a list from the user.

    def MakeList(self):
        print("Please enter your list [separate the values, floats only, with spaces]")
        print("\nList :",end=" ")
        try:
            List = [float(item) for item in input().split()]
        except:
            print("\nInput Error ---- [Restarting Choice]")
            List = self.MakeList()
        newList = []
        for cur in List:
            if cur%1 == 0:
                newList.append(int(cur))
            else:
                newList.append(cur)
        return newList

    ### This function is that allows a user to directly paste in previously used lists.

    def GetFullNetwork(self):
        try:
            network = input("List : ")
            tempList = network[2:-2].split("], [")
            newList = []
            for i in range(len(tempList)):
                Atemp = tempList[i].split(", ")
                Btemp = []
                for x in range(len(Atemp)):
                    Btemp.append(float(Atemp[x]))
                newList.append(Btemp)
            print(newList)
            if bfl.NetworkChecker(newList):
                return newList, len(newList[0])
            else:
                return self.GetFullNetwork()
        except:
            return self.GetFullNetwork()

    ### This simply gets the names of each node in the network.

    def NameList(self,NodeNo):
        print("")
        NodeNames = []
        for currentNode in range(NodeNo):
            print("Enter the name of node",currentNode+1,end=" : ")
            NodeNames.append(input())
        return NodeNames

    ### This is the network creation function.

    def MakeNetwork(self):
        network = []
        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("To create your network, please enter the number of nodes in your graph")
        try:
            NodeNo = int(input("\nNumber of nodes[Leave blank to paste whole network] : "))
        except:
            print("\nPlease enter the complete list(formatted the same as when copied)")
            network, NodeNo = self.GetFullNetwork()
            return network, self.NameList(NodeNo)

        for a in range(NodeNo):
            temp = []
            for b in range(NodeNo):
                temp.append(0)
            network.append(temp)

        NodeNames = self.NameList(NodeNo)

        for x in range(NodeNo-1):
            print("\nPlease enter the weight of the nodes connecting to",NodeNames[x],"[If there is no connection leave blank]\n")
            for y in range(NodeNo):
                if x < y:
                    print("The weight of connection between",NodeNames[x],"and",NodeNames[y],end=" : ")
                    try:
                        currentWeight = float(input())
                        network[x][y] = currentWeight
                        network[y][x] = currentWeight
                    except:
                        pass

        bfl.NetworkChecker(network)
        print("Network created :",network,"\n\n")
        return network, NodeNames

### This class is the overarching class for the two shortest path algorithms.

class ShortestPathBot(NetworkBot):

    def __init__(self,network,NodeName):
        NetworkBot.__init__(self)
        self.algorName = "Timer"
        if network == 0 and NodeName == 0:                              # Gets the network if one has not been given #
            self.network, self.NodeNames = NetworkBot.MakeNetwork(self)
        else:
            self.network = network
            self.NodeNames = NodeName

    ### This starts the algorithm section and gets the start and end locations.

    def Input(self):
        print("\n-=-=-=-=-=-=-=-=-=-=",self.algorName,"=-=-=-=-=-=-=-=-=-=-\n")
        print("To start the algorithm on your network please enter a start and end location.\n")
        for i in range(len(self.network[0])):
            print("["+str(self.NodeNames[i]),"=",str(i)+"]",end=" ")
        print("")
        try:
            startLoc = int(input("Start Location(NodeNumber) : "))
            TargetLoc = int(input("End Location(NodeNumber) : "))
        except:
            startLoc, TargetLoc = self.Input()
        return startLoc, TargetLoc

    ### Outputs the list in a linear english form.

    def returnArc(self,List):
        print(self.NodeNames[List[0]],end="")
        del List[0]
        for i in List:
            print(" to",self.NodeNames[i],end="")
        print("")

    ### This function returns the sum of the given list of arcs.

    def SumList(self,List):
        sum = 0
        for i in range(len(List)-1):
            sum += self.network[List[i+1]][List[i]]
        return sum

    ### This outputs a given list of arcs using the two above functions.

    def Output(self,List):
        print("\n\n\t∴ Shortest path :",end=" ")
        self.returnArc(List[:])
        print("\t\t~ of weight :",self.SumList(List))

### This class is for Dijkstra's Algorithm.

class DijkstraBot(ShortestPathBot):

    def __init__(self,network,NodeName):
        ShortestPathBot.__init__(self,network,NodeName)
        self.algorName = "Dijkstra's Algorithm"
        self.DistanceStore = [0]*len(self.network)
        self.RouteStore = [""]*len(self.network)

    ### This functions calls all the other functions in order for Dijkstra to run properly.

    def Initialise(self):
        StartLoc, TargetLoc = self.Input()
        self.StartStore = StartLoc
        self.FinalList = self.DijkstraMain(StartLoc,TargetLoc,0)
        self.FinalList.reverse()
        self.Output(self.FinalList)

    ### This function similar to the above function except it measures the run time.

    def Timer(self,StartLoc,TargetLoc):
        timerStart = time.time()
        self.StartStore = StartLoc
        self.FinalList = self.DijkstraMain(StartLoc,TargetLoc,0)
        timerEnd = time.time()
        self.FinalList.reverse()
        self.Output(self.FinalList)
        print("\tDijkstra Time :",timerEnd-timerStart)

    ### This works back through the network to find the shortest route after being given the traversal list.

    def GetRoute(self,TargetLoc,TraversalList):
        TraversalList.append(TargetLoc)
        for point0 in range(len(self.DistanceStore)):
            if self.StartStore == TargetLoc:
                return TraversalList
            elif self.DistanceStore[TargetLoc] == self.DistanceStore[point0] + self.network[TargetLoc][point0] and point0 != TargetLoc:
                return self.GetRoute(point0,TraversalList)

    ### This the traversal list which is the shortest route from the start node to all the other nodes.

    def DijkstraMain(self,CurrentLoc,TargetLoc,PassNo):
        self.RouteStore[CurrentLoc] = PassNo

        ### Gets working value for each of the connected locations.
        for point1 in range(len(self.network)):
            TravelDistance = self.network[CurrentLoc][point1] + self.DistanceStore[CurrentLoc]
            if (self.DistanceStore[point1] > TravelDistance or self.DistanceStore[point1] == 0) and  self.RouteStore[point1] == "" and self.network[CurrentLoc][point1] != 0:
                self.DistanceStore[point1] = TravelDistance

        ### Determines the next current location.
        LowestValue = 0
        NextLoc = "Limit Reached"
        for point2 in range(len(self.network)):
            if self.RouteStore[point2] == "" and self.DistanceStore[point2] != 0 and (self.DistanceStore[point2] < LowestValue or LowestValue == 0) :
                LowestValue = self.DistanceStore[point2]
                NextLoc = point2

        ### Checks to see if target reached then passes to next iteration of the code.
        if NextLoc == TargetLoc:
            return self.GetRoute(TargetLoc,[])
        elif NextLoc == "Limit Reached" :
            return self.GetRoute(TargetLoc,[])
        else:
            return self.DijkstraMain(NextLoc,TargetLoc,PassNo+1)

### This is the class for the depth search algorithm.

class DepthBot(ShortestPathBot):

    def __init__(self,network,NodeName):
        ShortestPathBot.__init__(self,network,NodeName)
        self.algorName = "Depth Search Algorithm"

    ### This functions starts the depth search and then finds the shortest of the found routes.

    def Initialise(self):
        StartLoc, self.TargetLoc = self.Input()
        self.foundRoutes = []
        self.RecurSearch([StartLoc])
        shortest = self.foundRoutes[0]
        for current in self.foundRoutes:
            if self.SumList(current) < self.SumList(shortest):
                shortest = current
        self.Output(shortest)

    ### This function similar to the above function except it measures the run time.

    def Timer(self,StartLoc,TargetLoc):
        timerStart = time.time()
        self.TargetLoc = TargetLoc
        self.foundRoutes = []
        self.RecurSearch([StartLoc])
        shortest = self.foundRoutes[0]
        for current in self.foundRoutes:
            if self.SumList(current) < self.SumList(shortest):
                shortest = current
        timerEnd = time.time()
        self.Output(shortest)
        print("\tDepth Time :",timerEnd-timerStart)

    ### Returns all the arcs connected to a given node.

    def GetConnections(self,currentLoc):
        ConnectedArcs = []
        ArcList = bfl.GetArcListFromNetwork(self.network)
        for point in range(len(ArcList)):
            if currentLoc in ArcList[point]:
                ConnectedArcs.append(ArcList[point])
        return ConnectedArcs

    ### This recursively  looks through each possible route, which doesn't cycle, and then stores it.

    def RecurSearch(self,NodeList):
        possArcs =  self.GetConnections(NodeList[len(NodeList)-1])
        for i in possArcs:
            if i[0] in NodeList and i[1] in NodeList:
                possArcs.remove(i)

        for i in range(len(possArcs)):
            y, x = possArcs[i]
            if self.TargetLoc == x or self.TargetLoc == y:
                NodeList.append(self.TargetLoc)
                self.foundRoutes.append(NodeList[:])
            elif not(x in NodeList):
                nextList = NodeList[:]
                nextList.append(x)
                self.RecurSearch(nextList)
            elif not(y in NodeList):
                nextList = NodeList[:]
                nextList.append(y)
                self.RecurSearch(nextList)

