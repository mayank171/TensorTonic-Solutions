import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x=np.asarray(x)
    y=np.asarray(y)
    vals=np.pow((x-y),2)
    #print("x",x)
    #print("y",y)
    #print("hello",vals)
    summ=np.sum(vals)
    #print("sum",summ**0.5)
    return (summ**0.5)
    pass