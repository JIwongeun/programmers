def solution(arr):
    answer = 0
    
    while(1):
        check1 = 0
        check2 = 0
        for i, n in enumerate(arr):
            if n >= 50 and n%2==0:
                arr[i] = arr[i]/2
                check1 = 1
            elif n<50 and n%2==1:
                arr[i] = arr[i]*2 + 1
                check2 = 1
        
        if not(check1 or check2):
            break
        else:
            answer+=1
            
    return answer
    