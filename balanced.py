def IsBalanced(s):
    If len(s)%2!=0:
        return "Unbalanced"
    a=["[","{","("]
    b=["]","}",")"]
    c=[]
    for i in s:
        if i in a:
            c.append(i)
        elif i in b:
            d=b.index(i)
            if(len(c)>0 and a[d]==c[len(c)-1]):
                c.pop()
            else:
                return "Unbalanced"
    if len(c)==0:
        return "Balanced"
    else:
        return "Unbalanced"