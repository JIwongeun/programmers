def solution(date1, date2):
    answer = 0
    
    d1 = str(date1[0]) + str(date1[1]) + str(date1[2])
    d2 = str(date2[0]) + str(date2[1]) + str(date2[2])
    
    return int(int(d1) < int(d2))