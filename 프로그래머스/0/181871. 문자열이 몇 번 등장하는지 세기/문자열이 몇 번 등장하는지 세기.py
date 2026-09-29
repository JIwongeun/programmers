def solution(myString, pat):
   
    count = 0
    
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            count +=1
            i = i+len(pat)

    return count