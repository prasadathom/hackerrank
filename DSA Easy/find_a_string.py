#My solution for Find A String
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count = count +1    
    return count

#Best solution
