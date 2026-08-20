import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    array_x=np.asarray(x)
    array_y=np.asarray(y)
    # Write code here
    result = float(np.sum(np.abs(array_x - array_y)))
    return(result)
    pass
