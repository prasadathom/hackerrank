def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    walk=0
    for i in range(0,len(calorie)):
        walk= walk+calorie[i]*pow(2,i)
    return walk
