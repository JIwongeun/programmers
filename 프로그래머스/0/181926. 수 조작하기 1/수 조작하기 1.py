def solution(n, con):
    
    for c in con:
        if c == "w":
            n+=1
        elif c == "s":
            n-=1
        elif c == "d":
            n+=10
        else:
            n-=10

    
    
    return n