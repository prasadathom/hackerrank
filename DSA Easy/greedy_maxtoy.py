def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    n=len(prices)
    count=0
    for i in range(n):
        k=k-prices[i]
        if k>0:
            count = count+1
        else:
            return count
