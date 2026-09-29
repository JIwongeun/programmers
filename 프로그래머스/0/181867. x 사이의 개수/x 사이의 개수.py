def solution(myString):
    answer = []
    count = 0
    
    for i in range(len(myString)):
        if myString[i]!="x":
            count += 1
        else:
            answer.append(count)
            count = 0
            
    answer.append(count)
    
    return answer