import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    # np.ndarray_t = np.ndarray.T
    # HERE above we have to declare a matrix of the x dimensions and on the basis of it we need to make the transpose of tit !
    matrix = np.array(A)
    return matrix.T
    

    # print(ndarray_t)