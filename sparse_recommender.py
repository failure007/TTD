import pytest
from test_sparse_recommender import SparseMatrix  
# Import the SparseMatrix class from test_sparse_recommender.py

class TestSparseMatrix:
    
    #test set method
    def test_set(self):
        matrix = SparseMatrix()
        matrix.set(0, 0, 1)
        assert matrix.get(0, 0) == 1
        #This line asserts that the matrix value taken from row 0, column 0, is equal to 1. The test will not pass if this requirement is not satisfied

    # test get method
    def test_get(self):
        matrix = SparseMatrix()
        matrix.set(0, 0, 1)
        assert matrix.get(0, 0) == 1

    # test recommend method
    def test_recommend(self):
        matrix = SparseMatrix()
        matrix.set(0, 0, 1)
        vector = [1, 0, 0]
        assert matrix.recommend(vector) == [1, 0, 0]

    # test add_movie method
    def test_add_movie(self):
        matrix = SparseMatrix()
        matrix.set(0, 0, 1)
        othr_mat = SparseMatrix()
        othr_mat.set(0, 1, 1) 
        # Adjusted the other_matrix to have a value in the same position
        result = matrix.add_movie(othr_mat)
        # The value in the original matrix remains the same
        assert result.get(0, 0) == 1
        # The value from other_matrix is added
        assert result.get(0, 1) == 1

    # test to_dense method
    def test_to_dense(self):
        matrix = SparseMatrix()
        matrix.set(0, 0, 1)
        result = matrix.to_dense()
        assert result == [[1]]


    def test_recommend_large_matrix(self):
        matrix = SparseMatrix()
        #Fill the matrix with the value 1 in a 100x100 grid pattern
        for row in range(100):
            for col in range(100):
                matrix.set(row, col, 1)
        # create a vector with ones
        vector = [1] * 100
        # Obtain recommendations using the matrix and the vector
        result = matrix.recommend(vector)
        # Assert that the length of the result matches the size of the vector (100)
        assert len(result) == 100
