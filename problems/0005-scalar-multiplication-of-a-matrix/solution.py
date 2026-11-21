def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    scale = [[matrix[i][j]*scalar for j in range(len(matrix))] for i in range(len(matrix))]
    return scale