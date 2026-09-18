def solution(array, commands):
    answer = []
    for command in commands:
        s = command[0]
        e = command[1]
        i = command[2]
        tmp = array[s-1:e]
        tmp.sort()
        answer.append(tmp[i-1])
    return answer










def solution(array, commands):
    answer = []
    
    for command in commands:
        # i, j, k 변수 할당
        i = command[0]
        j = command[1]
        k = command[2]

        # array 자르기
        array_cut = array[i-1:j]

        # 정렬
        array_cut = sorted(array_cut)

        # 정답
        answer.append(array_cut[k-1])
        
    return answer