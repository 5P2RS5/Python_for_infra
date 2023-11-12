#!/bin/bash

# $1 : 프로그래머스 문제  레벨, $2 : 문제번호, $3 : 문제이름

echo $1"의" $2".py 파일 생성중...."
# 파일 생성하기
touch ~/documents/github/Python_for_infra/programmers/$1/$2.py

echo "README에 내용 추가중...."
# readme에 내용 추가하기 
# 문제번호 : 파일이름, 현재 날짜 시간(엔드라인을 위한 공백 두칸)
echo $2 ":" $3"," $(date)"  "  >> README.md

echo "작업 완료 문제를 푸십시오."
echo "⭐️⭐️⭐️화이팅⭐️⭐️⭐️"

