import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x=np.array(x)
    deno=1+np.exp(-x)
    return 1/deno

    pass