import pytest
from numpy import linalg,allclose,savetxt,loadtxt,array
from scipy.sparse import csr_matrix

class Matrix:
    def __init__(self,rows,cols,data=None):
        self.rows = rows
        self.cols = cols
        self.data = data if data is not None else array([[0 for i in range(cols)] for j in range(rows)])
        self.sparse_matrix = csr_matrix(self.data)
    
    def __add__(self,other):
        if self.rows == other.rows and self.cols == other.cols:
            matrix1 = Matrix(self.rows,self.cols)
            matrix1.sparse_matrix = self.sparse_matrix + other.sparse_matrix
            matrix1.data = matrix1.sparse_matrix.toarray()
            return matrix1
        else:
            raise ValueError("Wrong dimensions")

    def __sub__(self,other):
        if self.rows == other.rows and  self.cols == other.cols:
            matrix1 = Matrix(self.rows,self.cols)
            matrix1.sparse_matrix = self.sparse_matrix - other.sparse_matrix
            matrix1.data = matrix1.sparse_matrix.toarray()
            return matrix1
        else:
            raise ValueError("Wrong dimensions")
    
    def __mul__(self,other):
        if self.cols == other.rows:
            matrix1 = Matrix(self.rows,self.cols)
            matrix1.sparse_matrix = self.sparse_matrix.dot(other.sparse_matrix)
            matrix1.data = matrix1.sparse_matrix.toarray()
            return matrix1
        else:
            raise ValueError("Matrix is not square")

    def transport(self):
        matrix1 = Matrix(self.cols,self.rows)
        matrix1.sparse_matrix = self.sparse_matrix.T
        matrix1.data = matrix1.sparse_matrix.toarray()
        return matrix1
    
    def __eq__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return allclose(self.data, other.data)

    def __getitem__(self,index):
        return self.data[index]

    def determinant(self):
        return int(round(linalg.det(self.data)))
        
    def inverse(self):
        try:
            return linalg.inv(self.data)
        except:
            return "Matrix is not invertible"

    def eigenvalues(self):
        return linalg.eig(self.data)[0]

    def is_symmetric(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Wrong dimensions")
        return allclose(self.data, other.data)

    def load_matrix_from_csv(self,filename):
        try:
            self.data = loadtxt(filename,delimiter=',')
        except FileNotFoundError:
            print(f"File {filename} not found")
            raise
    
    def save_matrix_to_csv(self,filename):
        
        savetxt(filename,self.data,delimiter=',')

    def visualize_matrix(self):
        result = []
        for i in self.data:
            result.append(' '.join(map(str,i)))
        return '\n'.join(result)










