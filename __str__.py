import numpy as np

class Matrix:
    def __init__(self,rows,cols,data=None):
        self.rows = rows
        self.cols = cols
        self.data = data if data is not None else np.array([[0 for i in range(cols)] for j in range(rows)])

    
    def visualize_matrix(self):
        result = []
        for i in self.data:
            result.append(' '.join(map(str,i)))
        return '\n'.join(result)
    
    def __str__(self):
        return self.visualize_matrix()








