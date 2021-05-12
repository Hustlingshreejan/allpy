import numpy as np


A = np.array([[1,2],[1,22],[17,13]])
print(A)


def get_inverse(A):
    shape = A.shape
    if shape[0] == shape[1]:
        if np.linalg.matrix_rank(A) == shape[1]:
            print(np.linalg.inv(A))
            print('The matrix inverse is correct as it is giving an identity matrix', np.matmul(np.linalg.inv(A),A))
            return np.linalg.inv(A)

        else:
            print("pseudo inverse needs to be calculated")
    else:
        if shape[0] > shape[1]:
            print(np.linalg.matrix_rank(A))
            if np.linalg.matrix_rank(A) == shape[1]:
                print("As the matrix has row larger than column, calculating the left inverse")
                A_transpose = np.transpose(A)
                A_transpose_multiplyA = np.matmul(A_transpose, A)
                inverse_of_A_transpose_multiplyA = np.linalg.inv(A_transpose_multiplyA)
                A_inverse = np.matmul(inverse_of_A_transpose_multiplyA, A_transpose)
                print(A_inverse)
                print("checking whether the inverse is correct or not by multiplying the A with its inverse to get "
                      "identity matrix")
                print(np.matmul(A_inverse, A))
                return A_inverse

            else:
                print("pseudo inverse needs to be calculated")
        else:
            if np.linalg.matrix_rank(A) == np.shape[0]:
                print("As the matrix has row smaller than column, calculating the right inverse")

            else:
                print("pseudo inverse needs to be calculated")

            pass


get_inverse(A)

