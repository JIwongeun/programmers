def solution(str_list, ex):
    answer = "".join([n for n in str_list if ex not in n])
    return answer