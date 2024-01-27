
def initialise_2d_matrix(len_1, len_2):

    matrix = []

    for i in range(len_1):
        row = []
        for j in range(len_2):
            row.append(0)
        matrix.append(row)

    return matrix

def print_matrix(matrix):

    for i in range(len(matrix)):
        print(matrix[i])