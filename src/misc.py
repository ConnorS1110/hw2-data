def kap(listOfCols, fun): # t is 
    u = {}
    for k, v in enumerate(listOfCols):
        v, k = fun(v)
        u[k or len(u)+1] = v
    return u