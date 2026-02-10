import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x=np.asarray(x,dtype=float)

    ans=[]
    for val in x:
        if val==0:
            ans.append(1-p)
        else:
            ans.append(p)

    ans=np.asarray(ans,dtype=float)

    return (ans,p,p*(1-p))
    pass