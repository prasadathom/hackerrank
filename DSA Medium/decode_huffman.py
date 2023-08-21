def decodeHuff(root, s):
    #Enter Your Code Here
    cur = root
    chararray = []
    
    for c in s:
        if c == '0' and cur.left:
            cur = cur.left
        elif cur.right:
            cur = cur.right
        
        if cur.left == None and cur.right == None:
            chararray.append(cur.data)
            cur = root
    
    #Print final array
    print("".join(chararray))
