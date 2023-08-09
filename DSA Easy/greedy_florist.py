def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    previous_purchase = 0
    for i in range(n):
        cost += (previous_purchase +1) * c[i]
        if (i+1)%k==0:
            previous_purchase += 1
    return cost
