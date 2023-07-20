def preOrder(root):
    #Write your code here
    p = root
    if p is None:
        return
    print(p.info, end=' ')
    preOrder(p.left)
    preOrder(p.right)
