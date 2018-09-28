def func(inlist):
    outdict = {}
    resdict ={}
    for i in inlist:
        outdict[i] = inlist.count(i)
        if outdict[i] ==1:
           resdict[i] = outdict[i]
    return outdict,resdict
print(func([1,2,2,3,5,6,5]))