def solution(s):
    num = {0 : "zero", 1 : "one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    for i in range(num) :
        if s.find(num[i]) >= 0 :
            s.replace(num.keys()[i], num.get(num[i]))
    return s