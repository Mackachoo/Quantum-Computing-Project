import copy

### This is the class that contains all the matrices operations algorithms.

class MatrixBot():

    def __init__(self):
        pass

    ### This initializer only gets the choice of operator from the user then passes them to the appropriate function.

    def Initialise(self):
        print("\n\n-=-=-=-=-=-=-=-=-=-= Matrices =-=-=-=-=-=-=-=-=-=-\n")
        print("Do you want to add(1), multiply(2) or inverse(3) a matrix : ",end="")
        try:
            choice = int(input())
            if choice == 1:
                sumMatrix = self.matrixAdder()
                self.PrintMatrix(sumMatrix)
            elif choice == 2:
                multiMatrix = self.matrixMultiplierInitialiser()
                self.PrintMatrix(multiMatrix)
            elif choice == 3:
                InvMatrix = self.matrixInverserComplex()
                self.PrintMatrix(InvMatrix)
            else:
                int("Hqak ak kiddikeg hi wbeew : Bombarda")
        except:
            return self.Initialise()


    ### Adds two matrices of the same dimension!

    def matrixAdder(self):
        x,y = self.GetDimensions()
        MatrixA = self.CreateMatrix(x,y)
        self.PrintMatrix(MatrixA)
        MatrixB = self.CreateMatrix(x,y)
        self.PrintMatrix(MatrixB)
        MatrixNew = self.CreateBlank(x,y)
        for yLoc in range(y):
            for xLoc in range(x):
                MatrixNew[yLoc][xLoc] = MatrixA[yLoc][xLoc] + MatrixB[yLoc][xLoc]
        return MatrixNew


##### Inverting n x n Matrices !

    ### This takes a matrix and removes all values on the same row and column of a position, then returns the matrix.

    def removeAdjacent(self,tempMatrix,X,Y):
        del tempMatrix[Y]
        for i in range(len(tempMatrix)):
            del tempMatrix[i][X]
        return tempMatrix

    ### This function works out the determinant of a matrix.

    def GetDeterminant(self,Matrix):
        if len(Matrix[0]) == 1:
            return Matrix[0][0]
        elif len(Matrix[0]) == 2:
            return Matrix[0][0]*Matrix[1][1]-Matrix[0][1]*Matrix[1][0]
        else:
            tempNum = 0
            for rNum, rItem in enumerate(Matrix[0]):
                tempNum += (1-2*(rNum%2))*rItem*self.GetDeterminant(self.removeAdjacent(copy.deepcopy(Matrix),rNum,0))
            return tempNum

    ### This is the function that, using the above functions, works out the inverse matrix from the user input.

    def matrixInverserComplex(self):
        print("\nPlease enter matrix dimensions (n x n) :")
        N = int(input("N : "))
        Matrix = self.CreateMatrix(N,N)
        self.PrintMatrix(Matrix)
        determinant = self.GetDeterminant(Matrix)
        print("\n\tThe matrix determinant was",str(determinant)+".")
        MatrixN = self.CreateBlank(N,N)

        for yLoc in range(N):
            for xLoc in range(N):
                MatrixN[yLoc][xLoc] = (1/determinant)*(1-2*((xLoc+yLoc)%2))*self.GetDeterminant(self.removeAdjacent(copy.deepcopy(Matrix),yLoc,xLoc))
        return MatrixN


##### Matrix multiplication!

    ### This is effectively the initializer for matrix multiplication, so it takes the users choice and runs it.

    def matrixMultiplierInitialiser(self):
        print("\n\tPlease enter whether you want to multiply two matrices(1) or multiply a matrix by a constant(2) :",end=" ")
        try:
            choice =  int(input())
            if choice == 1:
                return self.matrixMultiplierComplex()
            elif choice == 2:
                return self.matrixMultiplierSimple()
            else:
                int("ផ្ទុះ")
        except:
            return self.matrixMultiplierInitialiser()

    ### Multiplies a matrix by a constant.

    def matrixMultiplierSimple(self):
        try:
            x,y = self.GetDimensions()
            Matrix = self.CreateMatrix(x,y)
            num = float(input("Enter number to multiply :"))
            self.PrintMatrix(Matrix)
            for yLoc in range(y):
                for xLoc in range(x):
                    Matrix[yLoc][xLoc] = Matrix[yLoc][xLoc]*num
            return Matrix
        except:
            return self.matrixMultiplierSimple()

    ### Multiplies two matrices, however is mainly just a passing function taking user input to the maths function.

    def matrixMultiplierComplex(self):
        x,y = self.GetDimensions()
        MatrixA = self.CreateMatrix(x,y)
        self.PrintMatrix(MatrixA)
        MatrixB = self.CreateMatrix(y,x)
        self.PrintMatrix(MatrixB)

        return self.MatrixComp(x,y,MatrixA,MatrixB)

    ### This is the function that actually multiplies the two matrices and is called by above function.

    def MatrixComp(self,minVal,maxVal,HighMatrix,LowMatrix):
        MatrixM = self.CreateBlank(minVal,minVal)
        for A in range(len(MatrixM)):
            for B in range(len(MatrixM)):
                temp = 0
                for add in range(maxVal):
                    temp += HighMatrix[add][B]*LowMatrix[A][add]
                MatrixM[A][B] = temp
        return MatrixM

##### ----------------------------------------------------------------------------------------------------------------

    ### This creates an n x n identity matrix.

    def CreateIdentity(self,n):
        Matrix  = self.CreateBlank(n,n)
        for i in range(n):
            Matrix[i][i] = 1
        return Matrix

    ### This creates an X x Y blank matrix.

    def CreateBlank(self,X,Y):
        blank = []
        for a in range(Y):
            temp = []
            for b in range(X):
                temp.append(0)
            blank.append(temp)
        return blank

    ### This function prints matrices.

    def PrintMatrix(self,Matrix):
        print("")
        for a in range(len(Matrix)):
            print("| ",end="")
            for b in range(len(Matrix[a])-1):
                print(round(Matrix[a][b],3),end=", ")
            print(round(Matrix[a][len(Matrix[a])-1],3),"|")
        print("")

    ### A simple function for getting user input of the dimensions.

    def GetDimensions(self):
        try:
            print("\nPlease enter matrix dimensions :")
            x = int(input("X : "))
            y = int(input("Y : "))
            return x,y
        except:
            return self.GetDimensions()

    ### This gets user input and turns it into a correctly formatted matrix for the other functions to use.

    def CreateMatrix(self,x,y):
        Matrix = self.CreateBlank(x,y)
        print("Now enter the matrix items(row then collumn)[{},{}]".format(x,y))
        for yLoc in range(y):
            for xLoc in range(x):
                output = "Please enter item at point ("+str(xLoc)+","+str(yLoc)+") (leave blank for zero): "
                try:
                    Matrix[yLoc][xLoc] = float(input("Please enter item at point ({},{}) (leave blank for zero): ".format(xLoc+1,yLoc+1)))
                except:
                    pass
        return Matrix

