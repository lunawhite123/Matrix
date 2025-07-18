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