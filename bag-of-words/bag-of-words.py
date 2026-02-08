import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    d={}
    for s in tokens:
        d[s]=d.get(s,0)+1

    res=[d.get(word,0) for word in vocab]

    res=np.asarray(res,dtype=int)
    return res
    pass