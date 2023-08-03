def minimumAbsoluteDifference(arr):
    # Write your code here
    min=abs(arr[0]-arr[1]) 
    n =len(arr)
    for i in range(0,n):
         for j in range(0,n):
            sub=abs(arr[i]-arr[j])
            if i!=j and sub < min :
                min = sub
    
    return min


def minimumAbsoluteDifference(arr):
    mindiff = []
    arr.sort()
    for i in range(len(arr)-1):
        mindiff.append(abs(arr[i]-arr[i+1]))
    return min(mindiff)
