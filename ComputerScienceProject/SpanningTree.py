import BasicFunctionsLibrary as bfl

### This is the class for Primm's algorithm.

class PrimmBot():

    def __init__(self,Matrix,NodeNames):
        self.Matrix = Matrix
        self.NodeNames = NodeNames
        print("\n-=-=-=-=-=-=-=-=-=-= Primm's Algorithm =-=-=-=-=-=-=-=-=-=-\n")
        for i in range(len(self.Matrix[0])):
            print("["+str(self.NodeNames[i]),"=",str(i)+"]",end=" ")
        print("")

    ### Gets user input for starting point then runs Primm's algorithm througth the other functions.

    def Initialise(self):
        try:
            self.NodeList = [int(input("\nPlease enter the number of the starting point : "))]
            print("")
        except:
            self.Initialise()
        while len(self.NodeList) != len(self.NodeNames):
            nextArc = self.GetNextArc()
            for i in range(2):
                if not nextArc[i] in self.NodeList:
                    self.NodeList.append(nextArc[i])
            print("Add arc of weight",self.Matrix[nextArc[0]][nextArc[1]],"between nodes",self.NodeNames[nextArc[0]],"and",self.NodeNames[nextArc[1]],"to the network")

    ### This looks through all the arcs and finds the lowest one, which won't create a loop, to return.

    def GetNextArc(self):
        curConArcs = []
        for i in range(len(self.NodeList)):
            curConArcs.extend(self.GetConnections(self.NodeList[i]))
        possArcs = self.RemovePairs(curConArcs)

        MinArc = "One fine day in the middle of the night!"
        for point in range(len(possArcs)):
            y, x = possArcs[point]
            if not(y in self.NodeList and x in self.NodeList):
                if MinArc == "One fine day in the middle of the night!":
                    MinArc = self.Matrix[y][x]
                    currArc = [y,x]
                elif self.Matrix[y][x] < MinArc:
                    MinArc = self.Matrix[y][x]
                    currArc = [y,x]
        return currArc

    ### Removes pairs from a list.

    def RemovePairs(self,List):
        for i in range(len(List)):
            try:
                if List[i] in List[:i]:
                    dupe = List[i]
                    List = bfl.delListShift(bfl.delListShift(List,dupe),dupe)
            except:
                pass
        return List

    ### Returns all the arcs connecting to the given node.

    def GetConnections(self,currentLoc):
        ConnectedArcs = []
        ArcList = bfl.GetArcListFromNetwork(self.Matrix)
        for point in range(len(ArcList)):
            if currentLoc in ArcList[point]:
                ConnectedArcs.append(ArcList[point])
        return ConnectedArcs

### This is the class for Kruskal's Algorithm.

class KruskalBot():

    def __init__(self,Matrix,NodeNames):
        self.Matrix = Matrix
        self.NodeNames = NodeNames
        self.OrderedList = []

    ### This function checks to see if a loop would be created if the arc between A and B would be added to the new network.

    def LoopChecker(self,checkList,pointA,pointB,attempts):
        if pointA == pointB:
            self.GlobalBoolean = False
        elif attempts != len(checkList):
            for index in range(len(checkList)):
                try:
                    currentLoc = checkList[index].index(pointA)
                    self.LoopChecker(checkList,checkList[index][1-currentLoc],pointB,attempts+1)
                except:
                    pass

    ### This is the function that runs the algorithm using the other functions and then prints the results.

    def ArcAdder(self):
        checkList = []
        for count in range(len(self.OrderedList)):
            y, x = self.OrderedList[count]
            self.GlobalBoolean = True
            self.LoopChecker(checkList,self.OrderedList[count][0],self.OrderedList[count][1],0)
            if self.GlobalBoolean:
                print("Add arc of weight",self.Matrix[y][x],"between nodes",self.NodeNames[self.OrderedList[count][0]],"and",self.NodeNames[self.OrderedList[count][1]],"to the network")
                checkList.append(self.OrderedList[count])

    ### This function puts the arc in order it in terms of weight, using a system similar to bubble sort.

    def Positioner(self,current,checkLoc):
        y, x = self.ArcList[current]
        yp, xp = self.OrderedList[checkLoc]
        if self.Matrix[y][x] >= self.Matrix[yp][xp]:
            self.OrderedList.insert(checkLoc+1,self.ArcList[current])
        elif checkLoc == 0:
            self.OrderedList.insert(checkLoc,self.ArcList[current])
        else:
            self.Positioner(current,checkLoc-1)

    ### This function gets the arc list and puts them in a list, using the above function to order it.

    def GetArcsIndex(self):
        self.ArcList = bfl.GetArcListFromNetwork(self.Matrix)

        for count in range(len(self.ArcList)):
            if count == len(self.ArcList):
                return self.OrderedList
            elif count == 0:
                self.OrderedList.append(self.ArcList[count])
            else:
                self.Positioner(count, len(self.OrderedList)-1)

    ### This sets of the algorithm.

    def Initialise(self):
        print("\n\n-=-=-=-=-=-=-=-=-=-= Kruskal's Algorithm =-=-=-=-=-=-=-=-=-=-\n")
        self.GetArcsIndex()
        print("The arcs in order :",self.OrderedList,"\n")
        self.ArcAdder()

