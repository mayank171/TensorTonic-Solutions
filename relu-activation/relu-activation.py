import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    y=np.maximum(0,x)
    if y.ndim==0:
        return y.reshape(1)
    return y
    pass