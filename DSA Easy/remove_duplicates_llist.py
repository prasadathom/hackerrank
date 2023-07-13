def removeDuplicates(llist):
    # Write your code here
    temp_head= llist
    dup=temp_head.next
    while temp_head != None and dup != None:
        if temp_head.data == dup.data:
            dup=dup.next
            temp_head.next=dup
        else:
            temp_head=temp_head.next
            dup=dup.next
                   
    return llist
