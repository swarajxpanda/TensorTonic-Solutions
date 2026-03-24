import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    f_x = 1 / (1 + np.exp(-np.array(x)))
    return f_x