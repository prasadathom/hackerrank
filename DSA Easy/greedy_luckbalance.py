def luckBalance(k, contests):
    # Write your code here
    imp=[]
    uimp=[]
    for i in range(0,len(contests)):
        if contests[i][1]==1:
            imp.append(contests[i][0])
        else:
            uimp.append(contests[i][0])
    
    imp.sort(reverse=True)
    sum_uimp=sum(uimp)
    sum_imp=0
    for i in range(0,len(imp)):
        if i < k :
            sum_imp=sum_imp+imp[i]
        else:
            sum_imp=sum_imp-imp[i]
    
    tsum=sum_imp+sum_uimp
    
    return tsum
