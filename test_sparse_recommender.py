class SparseMatrix:

    def __init__(self):
        self.data = {}  # Initialize an empty data dictionary to store sparse matrix values

    def set(self, row, col, value):
        self.data[(row, col)] = value  # Set the value at the given (row, col) position in the dictionary

    def get(self, row, col):
        return self.data.get((row, col), 0)  # Retrieve the value at the given (row, col) position or return 0 if not found

    def recommend(self, vector):
        result = []
        for row in range(len(vector)):
            value = 0
            for col in range(len(vector)):
                value += vector[col] * self.get(col, row)  # Calculate the recommendation value
            result.append(value)
        return result

    def add_movie(self, other_matrix):
        result = SparseMatrix()
        # Copy data from the original matrix
        for (row, col), value in self.data.items():
            result.set(row, col, value)
        # Add values from other_matrix
        for (row, col), value in other_matrix.data.items():
            result.set(row, col, result.get(row, col) + value)
        return result

    def to_dense(self):
        max_row, max_col = -1, -1
        for row, col in self.data.keys():
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        result = [[0] * (max_col + 1) for _ in range(max_row + 1)]

        for (row, col), value in self.data.items():
            result[row][col] = value  # Populate the dense matrix with values from the sparse matrix

        return result
