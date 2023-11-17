class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def set(self, row, col, value):
        if self._is_valid_index(row, col):
            self.data[(row, col)] = value
        else:
            raise ValueError

    def get(self, row, col):
        if self._is_valid_index(row, col):
            return self.data.get((row, col), 0)
        else:
            raise ValueError

    def recommend(self, user_vector):
        if len(user_vector) != self.cols:
            raise ValueError
        
        recommendations = [0] * self.rows
        
        for (row, col), value in self.data.items():
            recommendations[row] += value * user_vector[col]
        
        return recommendations

    def add_movie(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError

        for (row, col), value in other_matrix.data.items():
            self.set(row, col, self.get(row, col) + value)
            
        return self

    def to_dense(self):
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        
        return dense_matrix
    
    def _is_valid_index(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
