import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a=np.asarray(a)
    b=np.asarray(b)
    ab=np.dot(a,b)
    #print("dotab",ab)
    norma=np.linalg.norm(a)
    #print("moda",moda)

    normb=np.linalg.norm(b)
    #print("modb",modb)

    if norma==0 or normb==0:
        return 0
    
    return ab/(norma*normb)
    pass