#My solution for the Left Rotation
def rotateLeft(d, arr):
    sub1=arr[:d]
    sub2=arr[d:]
    sub2.extend(sub1)    
    return sub2
  
#Best solution should be mine(I hope ¯\_( ͡° ͜ʖ ͡°)_/¯)
