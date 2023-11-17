from sparse_recommender import SparseMatrix

def test_set_value():
    matrix = SparseMatrix(3, 4)
    
    matrix.set(0, 0, 1)
    
    assert matrix.get(0, 0) == 1

def test_get_value():
    matrix = SparseMatrix(3, 4)
    
    matrix.set(1, 1, 2)
    
    assert matrix.get(1, 1) == 2

def test_recommend():
    matrix = SparseMatrix(3, 4)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    
    vector = [1, 2, 0, 0]
    
    recommendations = matrix.recommend(vector)
    
    assert recommendations == [1, 4, 0]

def test_add_movie():
    matrix1 = SparseMatrix(3, 4)
    matrix1.set(0, 0, 1)
    
    matrix2 = SparseMatrix(3, 4)
    matrix2.set(1, 1, 2)
    
    result_matrix = matrix1.add_movie(matrix2)
    
    assert result_matrix.get(0, 0) == 1
    assert result_matrix.get(1, 1) == 2


def test_to_dense():
    matrix = SparseMatrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    
    dense_matrix = matrix.to_dense()
    
    assert dense_matrix == [[1, 0, 0], [0, 2, 0]]
