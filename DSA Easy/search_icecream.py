def icecreamParlor(m, arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and arr[i]+arr[j]==m:
                return i+1,j+1
