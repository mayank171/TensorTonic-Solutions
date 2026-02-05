import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v=np.asarray(v)
    n=len(v)
    a=np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i==j:
                a[i][j]=v[i]

    return a
    pass
