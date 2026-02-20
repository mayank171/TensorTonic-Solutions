import math
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    ans=[]
    for val in values:
        ct=degree
        res=[]
        for i in range(ct+1):
            res.append(math.pow(val,i))
        ans.append(res)

    return ans