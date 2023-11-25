def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for idx, citation in enumerate(citations, start=1):
        print(idx, citation)
        if idx <= citation:
            answer = idx
        else:
            break

    return answer

print(solution([1, 1, 2, 7, 9, 32]))