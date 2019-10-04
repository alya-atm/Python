def uniq(lts):
    res=[]
    for i in lst:
        if lst.count(i)>1 & res.count(i)==0:
            res.append(i)
        elif lst.count(i)==1:
            res.append(i)
        else:
            continue
    return res

lst=[1,'cat',3,2,4,4,5,1,8,9,3,'cat']
print(uniq(lst))