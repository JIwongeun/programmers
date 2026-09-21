from collections import Counter

def solution(a, b, c, d):
   
    answer = 0
    
    data = sorted(Counter([a,b,c,d]).items(), key = lambda x : x[1])
   
    if len(data) == 1:
        answer += 1111*data[0][0]
    elif len(data) == 2:
        if data [0][1] != data[1][1]:
            if data[0][1] > data [1][1]:   
                b = data[0][0]
                s = data[1][0]
            else:
                b = data[1][0]
                s = data[0][0]
            answer += (10*b + s)**2
        else:
            answer += (data[0][0] + data[1][0]) * abs((data[0][0] - data[1][0]))
    elif len(data) == 3:
        answer += data[0][0] * data[1][0]
    else:
        answer += min(a,b,c,d)
    
    return answer