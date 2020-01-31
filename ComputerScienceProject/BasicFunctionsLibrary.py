
### This error checks networks to confirm that the data is all correct.

def NetworkChecker(matrix):
    ErrorList = []
    Correct = True
    NoVertices = len(matrix)
    for y in range(NoVertices):
        for x in range(NoVertices):
            #print("Checking:",matrix[x][y],"+",matrix[y][x])
            if matrix[x][y] != matrix[y][x]:
                Correct = False
                ErrorList.append(str(y)+","+str(x))
    return Correct

### This function returns all the arcs from a network.

def GetArcListFromNetwork(Matrix):
    ArcList = []
    for y in range(len(Matrix)):
        for x in range(len(Matrix)):
            if Matrix[y][x] != 0 and x > y:
                ArcList.append([y,x])
    return ArcList

### This functions gets the mode of the list.

def HighestOccurrence(list,target):
    store = 0
    TopLoc = 0
    for i in range(len(list)):
        No = list[i].count(target)
        if No > store:
            store = No
            TopLoc = i
    return TopLoc

### This is a recursive algorithm for calculating binomial distributions to a specific order.

def BinomialDistribution():
    def FreakingRecursion(Row):
        if Row == 0:
            return [1]
        else:
            lastRow = FreakingRecursion(Row - 1)
            thisRow = []
            for index in range(0, len(lastRow) + 1):
                if index == 0 or (len(lastRow)) == index:
                    thisRow.append(1)
                else:
                    Value = lastRow[index] + lastRow[index - 1]
                    thisRow.append(Value)
            return thisRow

    order = int(input("\nEnter the order of binomial you want: "))
    PascalsList = FreakingRecursion(order - 1)

    print(PascalsList)

### This removes an item from a list and then shifts the rest of the list back to fill in the space.

def delListShift(List,target):
    tLoc = List.index(target)
    for point in range(len(List)):
        if point > tLoc:
            List[point-1] = List[point]
    List.pop()
    return List


