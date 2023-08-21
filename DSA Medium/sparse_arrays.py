def matchingStrings(stringList, queries):
    # Write your code here
    count=[0]*len(queries)
    for i in range(len(queries)):
        for j in range(len(stringList)):
            if stringList[j]==queries[i]:
                count[i]=count[i]+1
            
        
    return count
