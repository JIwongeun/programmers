def solution(my_string, s, e):
    return my_string.replace(my_string[s:e+1], my_string[s:e+1][::-1])