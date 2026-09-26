def solution(todo_list, finished):
    
    return [not_finished for i, not_finished in enumerate(todo_list) if not finished[i]]