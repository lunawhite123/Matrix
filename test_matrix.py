import numpy as np
import os
import pytest
from matrix import Matrix

def test_add():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix2 = Matrix(2,2,data=np.array([[5,6],[7,8]]))
    c = matrix1 + matrix2
    assert np.allclose(c.data,np.array([[6,8],[10,12]]))

def test_sub():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix2 = Matrix(2,2,data=np.array([[5,6],[7,8]]))
    c = matrix1 - matrix2
    assert np.allclose(c.data,np.array([[-4,-4],[-4,-4]]))
def test_mul():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix2 = Matrix(2,2,data=np.array([[5,6],[7,8]]))
    c = matrix1 * matrix2
    assert np.allclose(c.data,np.array([[19,22],[43,50]]))

def test_transport():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    c = matrix1.transport()
    assert np.allclose(c.data,np.array([[1,3],[2,4]]))

def test_eq():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix2 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert matrix1 == matrix2

def test_getitem():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert matrix1[0][0] == np.array(1)

def test_determinant():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert matrix1.determinant() == -2

def test_inverse():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert np.allclose(matrix1.inverse(),np.array([[-2,1],[1.5,-0.5]]))

def test_eigenvalues():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert np.allclose(matrix1.eigenvalues(),np.array([-0.37228132, 5.37228132]))

def test_is_symmetric():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix2 = Matrix(2,2,data=np.array([[1,2,3],[2,1,7]]))
    with pytest.raises(ValueError):
        matrix1.is_symmetric(matrix2)

def test_load_matrix_from_csv():
    matrix1 = Matrix(2,2)
    with pytest.raises(FileNotFoundError):
        matrix1.load_matrix_from_csv("matrix.csv")

def test_save_matrix_to_csv():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    matrix1.save_matrix_to_csv("matrix.csv")
    assert os.path.exists("matrix.csv")

def test_visualize_matrix():
    matrix1 = Matrix(2,2,data=np.array([[1,2],[3,4]]))
    assert matrix1.visualize_matrix() == "1 2\n3 4"













