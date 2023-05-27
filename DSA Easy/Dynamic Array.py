#My solution of Dyanmic Array
def dynamicArray(n, queries):
    arr=[[] for _ in range(n)]
    qlen=len(queries)
    lastanswer=0
    answer=[]
    for i in range(0,qlen):
        str(queries[i]).split()
        if queries[i][0] == 1:
            arr[(queries[i][1]^lastanswer)%n].append(queries[i][2])
        if queries[i][0] == 2:  
            lastanswer = arr[(queries[i][1]^lastanswer)%n][queries[i][2]%len(arr[(queries[i][1]^lastanswer)%n])]
            answer.append(lastanswer)
    return answer
 
#better solution of Dynamic Array
def dynamicArray(n, queries):

    last_answer = 0
    seq = [[] for _ in range(n)]

    for q in queries:
        op, x, y = q

        if op == 1:
            seq[(x ^ last_answer) % n].append(y)
        elif op == 2:
            s = seq[(x ^ last_answer) % n]
            last_answer = s[y % len(s)]
            print(last_answer)

        
    
