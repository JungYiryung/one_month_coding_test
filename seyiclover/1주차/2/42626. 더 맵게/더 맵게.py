import heapq

def solution(scoville, K):
    cnt = 0

    # 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)

    # 음식이 2개 이상이고, 최솟값이 K보다 작은 동안 반복
    while len(scoville) >= 2 and scoville[0] < K:

        # 가장 작은 두 음식 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 새로운 스코빌 지수 계산
        new = first + second * 2

        # 다시 힙에 넣기
        heapq.heappush(scoville, new)

        cnt += 1

    # 더 이상 섞을 수 없는데도 K보다 작다면 실패
    if scoville[0] < K:
        return -1

    return cnt