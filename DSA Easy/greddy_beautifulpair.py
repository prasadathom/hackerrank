def beautifulPairs(A, B):
    # Write your code here
    A.sort()
    B.sort()
    pair=0
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            if A[i]==B[j] and A[i]>0:
                pair=pair+1
                A[i]=0
                B[j]=0
                
    if pair < len(A):
       pair += 1
    else:
       pair -= 1
    return pair
