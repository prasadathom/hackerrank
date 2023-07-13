def getNode(llist, positionFromTail):
    # Write your code here
    elements=[]
    if llist==None:
        return None
    while llist != None:
        elements.append(llist.data)
        llist=llist.next
    
    n=positionFromTail
    relements=elements[::-1]
    return relements[n]
