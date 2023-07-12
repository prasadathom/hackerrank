def mergeLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    temp = None
    if head1.data < head2.data:
        temp = head1
        head1.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        head2.next = mergeLists(head1, head2.next)
    return temp
    
