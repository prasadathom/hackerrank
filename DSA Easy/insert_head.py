def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if llist == None:
        return SinglyLinkedListNode(data)
    else:
        new_node.next=llist
    return new_node


def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    if llist:
        node.next = llist
    return node
