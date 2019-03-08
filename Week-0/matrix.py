
class Matrix(object):
    
    def __init__(self, data):
        self.numRows = len(data)
        self.numColumns = len(data[0])
        self.data = data

    def show(self):

        for row in self.data:
            rowToShow = ""
            for column in row:
                rowToShow += "{:>10} ".format(column)
            print(rowToShow)

        print("")

    def add(self, matrixToAdd):
        if (isinstance(matrixToAdd,Matrix) == False):
            raise Exception("the element to add should be of type 'Matrix' ")

        if(self.numRows != matrixToAdd.numRows and self.numColumns != matrixToAdd.numColumns):
            raise Exception("the element to add should be {}x{}".format(self.numRows,self.numColumns))

        for i,row in enumerate(self.data):
            for j,column in enumerate(row):
                self.data[i][j] += matrixToAdd.data[i][j]
        
        print("the new matrix is...")
        self.show()

    
    def scalarMultiplication(self, scalar):
        for i,row in enumerate(self.data):
            for j,column in enumerate(row):
                self.data[i][j] *= scalar
        
        print("the new matrix is...")
        self.show()

    def multiply(self, matrixToMultiply):
        if (isinstance(matrixToMultiply,Matrix) == False):
            raise Exception("the element to add should be of type 'Matrix' ")

        if(self.numColumns != matrixToMultiply.numRows):
            raise Exception("the element to multiply should have {} columns".format(self.numRows))

        result = []
        calculatedRow = []
        
        for i in range(0,(self.numRows)):
            calculatedRow = []
            for j in range(0,(matrixToMultiply.numColumns)):
                rowSum = 0
                for k in range(0,(matrixToMultiply.numRows)):
                    rowSum += self.data[i][k] * matrixToMultiply.data[k][j]
                calculatedRow.append(rowSum)
            result.append(calculatedRow)
        self.data = result
        print("the result matrix is...")
        self.show()

    def transpose(self):
        result = []
        for j in range(0,(self.numColumns)):
            row = []
            for i in range(0,(self.numRows)):
                row.append(self.data[i][j])
            result.append(row)
        self.data = result
        print("the trasposed matrix is...")
        self.show()

    def determinant(self): # i have to validate nxn
        
        det = 0

        if(self.numRows == 2 and self.numColumns == 2):
            det = (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])
            return det

        if(self.numRows != self.numColumns):
            raise Exception("the matrix needs to be nxn.")

        #choose the better row to calculate the determinant, is the one that has max ceros count
        
        cerosCount = [item.count(0) for item in self.data]
        # print(cerosCount)
        betterRow = max(enumerate(cerosCount),key=lambda p: p[1],default=[0,0]) # ToDo: verify if the matrix doesn't have ceros !
        betterRowIndex = betterRow[0] 
        # print(betterRow)
        
        for j in range(0,(self.numColumns)):
            if(self.data[betterRowIndex][j]==0):
                continue
            cof = [[ colunm for k,colunm in enumerate(row) if k!=j] for i,row in enumerate(self.data) if i != betterRowIndex] #get the cofactor matrix. to do so, we eliminate the row what we have selected to work on and the column that it is being processed
            # print("---")
            cofMatrix = Matrix(cof)
            # cofMatrix.show()
            # print("...")
            
            det += ( Matrix.determinant(cofMatrix) * self.data[betterRowIndex][j]) * (-1 if(j%2 == 0) else 1)
        # print(det)
        return det
    
    def invert(self):
        #validate if the determinant is equals to 0 then the matrix cannot be enverted.
        pass

    def adjugate(self):
        pass
        
#########################################################

import pytest

matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix.show()

matrix2 = Matrix([[1,0,1],[0,2,2],[0,3,0]])
matrix2.show()

matrix3 = Matrix([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]])
matrix3.show()

matrix4 = Matrix([[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1],[13,14,15,1]])
matrix4.show()


matrix.add(matrix2)
matrix2.scalarMultiplication(2)
matrix3.multiply(matrix4)

matrix4.transpose()

matrix5 = Matrix([[1,-1],[3,-2]])
matrix5.show()
print(matrix5.determinant())

matrix6 = Matrix([[3,2,-1],[4,0,3],[2,-3,5]])
matrix6.show()
print(matrix6.determinant())

matrix7 = Matrix([[2,3,3,6],[2,3,6,7],[21,82,0,3],[2,23,1,1]])
matrix7.show()
print(matrix7.determinant())


def test_add():
    matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix2 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
    matrix.add(matrix2)
    assert matrix.data == [[2,3,4],[6,7,8],[10,11,12]]

def test_add_type_validation_someType():
    with pytest.raises(Exception):
        matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        matrix.add(5)

        
def test_add_type_validation_arrayType():
    with pytest.raises(Exception):
        matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        matrix.add([1,1,1])

def test_add_size_validation():
    with pytest.raises(Exception):
        matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        matrix2 = Matrix([[4,5,6],[7,8,9]])
        matrix.add(matrix2)

def test_scalarMultiplication():
    matrix = Matrix([[1,1,1],[2,2,2],[3,3,3]])
    matrix.scalarMultiplication(2)
    assert matrix.data == [[2,2,2],[4,4,4],[6,6,6]]

def test_multiply():
    matrix3 = Matrix([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]])
    matrix4 = Matrix([[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1],[13,14,15,1]])
    matrix3.multiply(matrix4)
    matrix3.show()
    assert matrix3.data == [[35,40,45,5],[70,80,90,10],[105,120,135,15]]

def test_multiply_type_validation():
    with pytest.raises(Exception):
        matrix3 = Matrix([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]])
        matrix3.multiply(5)

def test_multiply_size_validation():
    with pytest.raises(Exception):
        matrix3 = Matrix([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]])
        matrix4 = Matrix([[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]])
        matrix3.multiply(matrix4)

def test_transpose():
    matrix4 = Matrix([[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1],[13,14,15,1]])
    matrix4.transpose()
    assert matrix4.data == [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [1, 1, 1, 1, 1]]


def test_determinant_size_validation():
    with pytest.raises(Exception):
        matrix1 = Matrix([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]])
        matrix1.determinant()

def test_determinant_2x2():
    matrix5 = Matrix([[1,-1],[3,-2]])
    assert matrix5.determinant() == 1

def test_determinant_3x3():
    matrix6 = Matrix([[3,2,-1],[4,0,3],[2,-3,5]])
    assert matrix6.determinant() == 11


def test_determinant_4x4():
    matrix7 = Matrix([[2,3,3,6],[2,3,6,7],[21,82,0,3],[2,23,1,1]])
    assert matrix7.determinant() == -4627
