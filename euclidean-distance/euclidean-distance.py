import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    array_x = np.asarray(x)
    array_y = np.asarray(y)

    # result = float(np.sum(np.sqrt(np.abs(array_x,array_y))))

    squared_diff = (array_x - array_y) ** 2
    summed_diff = np.sum(squared_diff)
    result = float(np.sqrt(summed_diff))
    #so here the error was that the sum is done on the sqrt on diff
    #but the answer to the solution is that we need to first find the squared_diff then sum it and then srqt it then we get the final answer.
    
    return (result)
    pass