def has_cycle(head):
    if head == None:
        return 0
    i=0
    while head != None and i !=1001 :
        head= head.next
        i=i+1
            
    if head == None:
        return 0
    else:
        return 1
