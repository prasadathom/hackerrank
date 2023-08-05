def candies(n, arr):
    # Write your code here
    sum = 0
    ans = [1] * n

    if (n == 1):
        return 1

    for i in range(n - 1):
        if (arr[i + 1] > arr[i]):
            ans[i + 1] = ans[i] + 1
 
    for i in range(n - 2, -1, -1):
        if (arr[i] > arr[i + 1] and ans[i] <= ans[i + 1]):
            ans[i] = ans[i + 1] + 1
        sum =sum+ ans[i]
    sum =sum+ ans[n - 1]
    
    return sum

#remember a better way is to check from the back side
