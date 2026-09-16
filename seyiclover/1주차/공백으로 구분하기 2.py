def solution(my_string):
    answer = []
    my_string = my_string.strip().split(' ')
    for string in my_string:
        if string != "":
            answer.append(string)
    return answer