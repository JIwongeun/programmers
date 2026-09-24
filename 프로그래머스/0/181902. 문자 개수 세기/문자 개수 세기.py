def solution(my_string):
    answer = []
    
    for i in range(0, 26):
        answer.append(my_string.count(chr(ord('A') + i)))
        
    for i in range(0, 26):
        answer.append(my_string.count(chr(ord('a') + i)))
    
    return answer