def solution(arr, intervals):
    answer = []
    
    for rg in intervals:
        for i in arr[rg[0]:rg[1]+1]:
            answer.append(i)
    return answer