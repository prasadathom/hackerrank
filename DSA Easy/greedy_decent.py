def decentNumber(n):
    # Write your code here
    for fives in range(n, -1, -1):
        threes = n - fives
        if fives % 3 == 0 and threes % 5 == 0:
            
            return print("5" * fives + "3" * threes)
            
    print("-1")
