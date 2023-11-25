#!/bin/bash

# 프로그래머스 : 
# $1 : 문제 번호, $2 : 문제이름, $3 : 레벨
# 백준 : 
# $1 : 문제 번호, $2 : 문제 이름

if [ -z "$3" ]; then
    echo "[백준] 문제구나!"
    if [ -f "$HOME/documents/github/Python_for_infra/BOJ/$1.py" ] ; then
        echo "[$1 : $2]는 이미 풀었어!!, 또 풀어볼래?"
        read answer
        if [ "$answer" == "y" ] || [ "$answer" == "Y" ]; then
            echo "[$1 : $2]를 삭제할게 😅"
            rm "$HOME/documents/github/Python_for_infra/BOJ/$1.py"
        else
            echo "OK, 다음 문제로 넘어가자 🏃‍♂️"
            exit
        fi
    fi
    echo $1.py 파일 생성중....
    # 파일 생성하기
    touch $HOME/documents/github/Python_for_infra/BOJ/$1.py

    echo "README에 내용 추가중...."
    # readme에 내용 추가하기 
    # 문제번호 : 파일이름, 현재 날짜 시간(엔드라인을 위한 공백 두칸)
    echo "[백준] $1 : $2, $(date)" "  "  >> README.md

else
    echo "[프로그래머스] 문제구나!"
    echo $3"의" $1".py 파일 생성중...."

    # 폴더가 없을 때
    if [ ! -d "$HOME/documents/github/Python_for_infra/programmers/$3" ] ; then
        echo "폴더가 없습니다." $3"폴더를 생성합니다 🗂️"
        mkdir ~/documents/github/Python_for_infra/programmers/$1
    fi

    if [ -f "$HOME/documents/github/Python_for_infra/programmers/$3/$1.py" ] ; then
        echo "[$1 : $2]는 이미 풀었어!!, 또 풀어볼래?"
        read answer
        if [ "$answer" == "y" ] || [ "$answer" == "Y" ]; then
            echo "[$1 : $2]를 삭제할게 😅"
            rm "$HOME/documents/github/Python_for_infra/programmers/$3/$1.py"
        else
            echo "OK, 다음 문제로 넘어가자 🏃‍♂️"
            exit
        fi
    fi
    # 파일 생성하기
    touch $HOME/documents/github/Python_for_infra/programmers/$3/$1.py

    echo "README에 내용 추가중...."
    # readme에 내용 추가하기 
    # 문제번호 : 파일이름, 현재 날짜 시간(엔드라인을 위한 공백 두칸)
    echo "[프로그래머스] [Lv$3] $1 : $2, $(date)" "  "  >> README.md
fi
echo
echo "     "⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
echo "   작업 완료 했어 오늘도 화이팅이야!!"
echo "     "⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️