def levelOrder(root):
    myQ = [root]
    
    while(len(myQ) > 0):
        iter = myQ.pop(0)
        print(iter.info,end = " ")
        if (iter.left != None):
            myQ.append(iter.left)
        if (iter.right != None):
            myQ.append(iter.right)
