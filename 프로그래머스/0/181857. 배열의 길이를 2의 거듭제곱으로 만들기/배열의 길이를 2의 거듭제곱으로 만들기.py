def solution(arr):
  
    
    
    l = 1
    while len(arr) > l:
        l *= 2
    arr  = arr+ [0]*(int(l)-len(arr))   

    return arr