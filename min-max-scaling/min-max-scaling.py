def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    rows=len(data)
    cols=len(data[0])

    maxi=[]
    mini=[]
    for j in range(cols):
        maxii=0
        minii=1e9
        for i in range(rows):
            maxii=max(maxii,data[i][j])
            minii=min(minii,data[i][j])
        maxi.append(maxii)
        mini.append(minii)

    
    for i in range(rows):
        for j in range(cols):
            if maxi[j]-mini[j]==0:
                data[i][j]=0
            else :
                data[i][j]=(data[i][j]-mini[j])/(maxi[j]-mini[j])


    return data

            