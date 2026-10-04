def solution(rank, attendance):
    answer = 0
    
    p_s = [rank[i] for i, st in enumerate(attendance) if st]
    
    a, b, c = sorted(p_s)[:3]
    
    return 10000*rank.index(a) + 100*rank.index(b) + rank.index(c)