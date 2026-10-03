from collections import Counter

def solution(strArr):
    answer = 0
    
    lens = [len(st) for st in strArr]
    cnt = Counter(lens)
    
    
    return cnt.most_common(1)[0][1]