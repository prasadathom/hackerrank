def toys(w):
    # Write your code here
    w.sort()
    j=1
    min = w[0]+4
    
    for i in range(0,len(w)):
        if w[i]>min:
            min = w[i]+4
            j=j+1
            
    return j
