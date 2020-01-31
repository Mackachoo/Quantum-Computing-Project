import statistics
import math

### This is their because it is useful, not because it's a good example of anything.        <--- Do you think I should keep this, Sir?

def FreakingCoding(calcList):
    codedList = []
    additionFactor = float(input("Enter number to add(0 for no change) : "))
    divideNumber = float(input("Enter number to divide(1 for no change) : "))
    for i in range(len(calcList)):
        codedList.append((calcList[i]+additionFactor)/divideNumber)
    return codedList

def MidCorrerlater(list):
    squareList = []
    for a in range(len(list)):
        squareList.append(list[a]**2)
    ans = sum(squareList)-(sum(list))**2/len(list)
    return ans

def Correrlater(calcList):
    print("Enter second list :")
    newList = GetList()
    Scc = MidCorrerlater(calcList)
    Snn = MidCorrerlater(newList)
    additionList = []
    for V in range(len(calcList)):
        additionList.append(newList[V]*calcList[V])
    Snc = sum(additionList)-(sum(calcList)*sum(newList))/len(calcList)
    print("Scc :",round(Scc,1))
    print("Snn :",round(Snn,1))
    print("Snc :",round(Snc,1))

    print("Correlation Coefficient :",round(Snc/math.sqrt(Scc*Snn),3))

def PointPercentile(calcList):
    Pct = int(input("\nEnter percentile point : "))
    size = len(calcList)
    return sorted(calcList)[int(math.ceil((size * Pct) / 100)) - 1]

def QuartileRange(type,calcList):
    rangeSize = math.ceil(len(calcList)/4)
    if type == 0:
        return QuartileRange(3,calcList) - QuartileRange(1,calcList)
    else:
        return sorted(calcList)[int(math.ceil((len(calcList) * (type/ 4))))-1]


def GetList():
    return [float(item) for item in input().split()]

def Variance(calcList):
    squareList = []
    for a in range(len(calcList)):
        squareList.append(calcList[a]**2)
    σσ = (sum(squareList)/len(squareList))-(sum(calcList)/len(calcList))**2
    return σσ

def Start():
    try:
        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("\nEnter the list of numbers(space to seperate) :")
        StartMain(GetList())
    except:
        print("\nInput Error ---- [Restarting Choice]")

def StartMain(calcList):
    print("List :",calcList)
    print("Sorted List :",sorted(calcList))
    print("\nMean :",round(statistics.mean(calcList),2))
    print("Median :",statistics.median(calcList))
    try:
        print("Mode :",statistics.mode(calcList))
    except:
        pass
    print("\nUpper Quartile :",QuartileRange(3,calcList))
    print("InterQuartile :",QuartileRange(0,calcList))
    print("Lower Quartile :",QuartileRange(1,calcList))
    print("\nVariance(σ^2) :",round(Variance(calcList),2))
    print("Standard Deviation(σ) :",round(math.sqrt(Variance(calcList)),2))
    print("\nSkewness :",round(3*(statistics.mean(calcList)-statistics.median(calcList))/(math.sqrt(Variance(calcList))),3))
    print("\nUpper Outlier Range :",round(QuartileRange(3,calcList)+1.5*QuartileRange(0,calcList),2))
    print("Lower Outlier Range :",round(QuartileRange(1,calcList)-1.5*QuartileRange(0,calcList),2))

    Stay = True
    while Stay:
        choice = input("Options = Coding(C) or Correlator(R) or Percentiles(P) [Nothing to return to main menu] : ")
        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        choice.lower()
        if choice.upper() == "R":
            Correrlater(calcList)
        if choice.upper() == "C":
            StartMain(FreakingCoding(calcList))
        if choice.upper() == "P":
            print("Point :",PointPercentile(calcList))
        else:
            if choice != "":
                print("\nInput Error ---- [Restarting Choice]")
            Stay = False
