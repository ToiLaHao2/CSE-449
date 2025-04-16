# Q13. Python program to Multiply Two Matrices
def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result

def main():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    result = multiply_matrices(matrix_a, matrix_b)
    
    print("Resultant Matrix after Multiplication:")
    for row in result:
        print(row)
    return result

main()