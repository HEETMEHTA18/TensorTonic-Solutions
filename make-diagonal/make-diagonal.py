import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # # Write code here
    matrix = np.array(v)
    # np.zeros((0.5,0.5))
    # matrix(np.arrange(0.5))

    return np.diag(matrix)
    ## here we are just simply returning the diagonall of the array with teh np.arrya
    # pass