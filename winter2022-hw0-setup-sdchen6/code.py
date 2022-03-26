import numpy as np

def sum_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Sum two numbers.

    Args:
        x (int, float): first number in sum
        y (int, float): second number in sum
    Returns:
        Sum of x and y.
    """
    # replace the following line with an actual implementation that returns something
    return (x+y)

def multiply_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Multiply two numbers.

    Args:
        x (int, float): first number in product
        y (int, float): second number in product
    Returns:
        Product of x and y.
    """
    
    # replace the following line with an actual implementation that returns something
    return (x*y)

def create_add_matrix(x):
    """
    TODO: IMPLEMENT ME
    Step 1. Create a numpy array y whose elements all contain 1 
            This array y must be the same size as the input array x. 
    Step 2. Element-wise sum the two matrices to create a matrix z.
    Step 3. Return matrices y and z, in that order
    
    Args:
        x (np.ndarray): a 2D numpy array
    Returns:
        y (np.ndarray): the matrix of all 1s
        z (np.ndarray): the result of adding x and y, element-wise
    """

    # replace the following line with an actual implementation that returns something
    xshape = x.shape
    y = np.ones(xshape)
    z = np.add(x,y)
    return y, z

def indexing_aggregation(x, n):
    """
    TODO: IMPLEMENT ME
    Return the mean value of the first n elements of the input array x.

    Args:
        x (np.ndarray): a 1D numpy array
    Returns:
        output (float): the operation result

    """
    # replace the following line with an actual implementation that returns something
    sum = 0
    for i in range(0,n):
        sum += x[i]
    mean = sum/n
    return mean

  
