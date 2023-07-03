def insertNodeAtTail(head, data):
    new = head
    if head == None:
        return SinglyLinkedListNode(data)
    while new.next != None:
        new = new.next
    new.next = SinglyLinkedListNode(data)
    return head 
