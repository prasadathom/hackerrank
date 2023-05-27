#My solution to hourglass sum
def hourglassSum(arr):
    maxsum=-63  #-63 is necessary as the lowest possible sum for any hourglass is -63
    for i in range(0,4):
        for j in range(0,4):
            hsum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if hsum > maxsum:
                maxsum=hsum
    return maxsum
    
#best solution
