def isValid(s):
    # Count characters in the string
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1

    # Count the frequency of each count value
    count_dict = {}
    for value in char_dict.values():
        count_dict[value] = count_dict.get(value, 0) + 1

    # If all characters have the same frequency, return 'YES'
    if len(count_dict) == 1:
        return 'YES'

    # If there are two different frequencies
    elif len(count_dict) == 2:
        k1, k2 = count_dict.keys()
        if (count_dict[k1] == 1 and (k1 - 1 == k2 or k1 == 1)) or \
           (count_dict[k2] == 1 and (k2 - 1 == k1 or k2 == 1)):
            return 'YES'
    
    return 'NO'
