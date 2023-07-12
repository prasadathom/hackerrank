def compare_lists(llist1, llist2):
    temp1=llist1
    temp2=llist2
    if (temp1.data == None and temp2.data == None):
        return 1
    if (temp1.data == None or temp2.data == None):
        return 0
            
    while (temp1.next != None or temp2.next != None):
        if temp1.data != temp2.data:
            return 0
        else:
            temp1=temp1.next
            temp2=temp2.next
        if (temp1 == None and temp2 == None):
            return 1
        if (temp1 == None or temp2 == None):
            return 0

    if temp1.data==temp2.data:
        return 1
