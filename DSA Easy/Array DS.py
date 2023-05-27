#My solution for reversing a 1 D array
def reverseArray(a):
    n= len(a)
    r=[]
    for i in range(0,n):
        r.append(a[(n-1)-i])
    return r
           
           
#best solution
def reverseArray(a):
    return a[::-1]
