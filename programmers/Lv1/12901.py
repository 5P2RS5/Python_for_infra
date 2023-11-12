def solution(a, b):
    answer = ''
    arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = int(0)
    for i in range(1, a):
        result += int(arr[i])
    # 금 토 일 월 화 수
    
    result += int(b)

    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    
    answer = day[result % 7]
    
    
    
    return answer