import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    y=np.maximum(0,x)
    return y if y.ndim != 0 else y.reshape(1)
    pass