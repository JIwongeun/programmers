def solution(n):
    answer = 0
    if n%2==1:
        for i in range(n+1):
            answer += i if i%2==1 else 0
    else:
        for i in range(n+1):
            answer += i*i if i%2==0 else 0
            
    return answer