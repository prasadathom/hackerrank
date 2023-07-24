def balancedSums(arr):
    # Write your code here
    suma=sum(arr)
    for i in range(len(arr)):
        if sum(arr[:i])==sum(arr[i+1:]):
            return "YES"
        elif i == len(arr)-2:
            return "NO"





def balancedSums(arr):
    leftsum = 0
    total = sum(arr)
    for value in arr:
        if leftsum == total-value-leftsum:
            return "YES"
        leftsum+=value
    return "NO"
