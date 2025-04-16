# Q12. Python program to Add two Matrices
def add_matrices(matrix_a, matrix_b):
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def main():
    # Define two matrices
    matrix_a = [[1, 2, 3], [4, 6, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    # Add the matrices
    result = add_matrices(matrix_a, matrix_b)
    # Print the result
    print("Resultant Matrix after Addition:")
    for row in result:
        print(row)
    return result

main()