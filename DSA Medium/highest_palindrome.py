def highestValuePalindrome(s, n, k):
    s = list(s)
    
    changes = [0] * (n//2)
    
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            changes[i] = 1

            max_digit = max(s[i], s[n-1-i])
            s[i] = max_digit
            s[n-1-i] = max_digit
            k -= 1
    
    if k < 0:
        return '-1'
    
    i = 0
    while i < n//2 and k > 0:
        if s[i] != '9':
            if changes[i] and k >= 1:
                s[i] = s[n-1-i] = '9'
                k -= 1
            elif not changes[i] and k >= 2:
                s[i] = s[n-1-i] = '9'
                k -= 2
        i += 1
    
    if n % 2 and k > 0:
        s[n//2] = '9'
    
    return ''.join(s)
