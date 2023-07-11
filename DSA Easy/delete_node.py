def deleteNode(llist, position):
    if position == 0:
        return llist.next
    current = llist
    for i in range(position-1):
        current = current.next
    current.next = current.next.next   
    return llist
