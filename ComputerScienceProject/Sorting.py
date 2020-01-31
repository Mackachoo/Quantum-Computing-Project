
### This is the function which does bubble sort.

def BubbleBot(List):
    for passNo in range(len(List)-1,0,-1):
        for index in range(passNo):
            if List[index]>List[index+1]:
                tempItem = List[index]
                List[index] = List[index+1]
                List[index+1] = tempItem
    return List

### This is the class for Cycle Sort.

class CycleBot():

    def __init__(self,List):
        self.List = List

    ### This is the function which actually does the sort.

    def Initialise(self):
        for cycLoc in range(len(self.List)):    # Runs through each item in list #
            pos = cycLoc + 1
            while pos != cycLoc:
                pos = cycLoc
                for index in self.List[cycLoc+1:]:      # Searches through rest of the list to see how many are items are greater than the cycLoc #
                    if index < self.List[cycLoc]:
                        pos += 1
                if pos != cycLoc:
                    while self.List[cycLoc] == self.List[pos]:  # Checks that the location found is not already occupied by a value equal to the original #
                        pos += 1
                    self.List[pos], self.List[cycLoc] = self.List[cycLoc], self.List[pos]   # Swaps the original with the new point #

        return self.List

### This is the class for quick sort.

class QuickBot():

    def __init__(self,List):
        self.List = List

    ### This function only starts the computing function.

    def Initialise(self):
        toWork = input("Enter (0) for working otherwise leave blank: ")
        return self.QuickRecur(self.List,toWork)



    ### This is the computing function for quick sort.

    def QuickRecur(self,currentList,working):
        if len(currentList) <= 1:
            return currentList
        else:
            pivot = currentList[len(currentList)//2]    # Finds the pivot for the list #
            ListX = []
            ListE = []
            ListN = []
            for index in currentList:   # This for works through each item in the list and assigns it the correct list #
                if index > pivot:
                    ListX.append(index)     # For values greater than the pivot #
                elif index == pivot:
                    ListE.append(index)     # For values equal to the pivot #
                else:
                    ListN.append(index)     # For values less than the pivot #

            if working == "0":
                print("\nFor list:",currentList,"with pivot",ListE[0])
                ListT = [ListN,ListE,ListX]
                print("Splits into |",end=" ")
                for num in range(3):
                    if len(ListT[num]) > 0:
                        print(ListT[num],"|",end=" ")
                print("")

            return self.QuickRecur(ListN,working) + ListE + self.QuickRecur(ListX,working)      # This returns the lists in order but also recursively orders those lists independently #