def copyWithLimits(a,us,os):
    b = []
    for i in a:
        if (i > us) and (i < os):
            b.append(i)
    return b

a = [1,2,3,4,5,6,7,8,9]
print(copyWithLimits(a,3,7))
