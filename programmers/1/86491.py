def solution(sizes):
    answer = 0
    max = 0
    max2 = 0
    for i in range(0, len(sizes)) : 
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if(max < sizes[i][0]):
            max = sizes[i][0]
        if(max2 < sizes[i][1]):
            max2 = sizes[i][1]

    return max * max2