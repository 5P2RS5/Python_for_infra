def solution(s):
    answer = True
    
    a = int(0)
    b = int(0)
    
    a += int(s.count("p"))
    a += int(s.count("P"))

    b += int(s.count("y"))
    b += int(s.count("Y"))
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(a)
    print(b)
    return a == b