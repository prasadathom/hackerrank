def maximumPerimeterTriangle(sticks):
    peri = [-1]
    sticks = sorted(sticks, reverse=True)
    
    
    for i in range(2, len(sticks)):
        for j in range(1, i):
            for k in range(0, j):
                a=sticks[i]
                b=sticks[j]
                c=sticks[k]
                if a < b+c and b < c+a and c < a+b:
                    peri = (a, b, c)
                    return peri
                    
    return peri
