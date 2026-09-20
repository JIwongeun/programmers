def solution(arr, queries):
    for q in queries:
        i1, i2 = q[0], q[1]
        arr[i1], arr[i2] = arr[i2], arr[i1]
    
    return arr