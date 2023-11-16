def solution(lottos, win_nums):
    dic = {'8':1, '7':1, '6':1, '5':2, '4':3, '3':4, '2':5, '1':6, '0':6}
    answer = []
    same = 0
    zero = lottos.count(0)

    print(zero)
    for i in lottos : 
        for j in win_nums:
            if i == j :
                same += 1
    print(same)

    answer.append(dic[str(same + zero)])
    answer.append(dic[str(same)])

    return answer