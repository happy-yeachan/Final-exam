#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20191879 이름 : 오예찬

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    answer = 0
    # my_string이라는 문자열이 target문자열에 존재한다면
    if target in my_string: 
        # answer를 1로 지정
        answer = 1
    # 위 조건문에 걸리지 않았으면 0, 걸렸으면 1 반환
    return answer

# print(solution("asdfabcv", "abc"))

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    answer = ''
    # 모스부호는 공백으로 나누어져 있으니 이를 다루기 쉽게 리스트로 변환 (공백 단위로 자름)
    letter = list(letter.split())
    # letter 리스트의 요소를 하나씩 가져와 i에 대입 하며 아래 문장 실행 반복
    for i in letter:
        # morse 딕셔너리에서 모스부호를 key값으로 가지는 value(알파벳)값을 가져와 answer 문자열에 이어붙임
        answer += morse[i]
    # 완성된 문자열 출력
    return answer

# print(solution(".. .-.. --- ...- . ..-"))

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    # 문자열로 형 변환을 해주어 각 자릿수마다 다루기 쉽게 만들어줌
    age = str(age)
    # age 문자열의 길이만큼 반복하는 반복문
    for i in range(len(age)):
        # 숫자에 97을 더하고 이를 아스키코드로 생각하고 문자로 변환 후 answer 문자열에 이어붙임
        answer += chr(int(age[i])+97)
    # 완선된 answer문자열 반환
    return answer

# print(solution(24))

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    # 작은 원 안의 점 개수와 테두리 위의 점 개수 
    r1_point, dup_point = get_point(r1)
    # 큰 원 안의 점 개수
    r2_point, tmp = get_point(r2)
    # 큰 원 안의 점 개수 - 작은 원 안의 점 개수 + 작은 원 테두리 위의 점 개수
    answer = r2_point - r1_point + dup_point
    return answer

# 원 안에 존재하는 정수좌표의 개수를 반환하는 함수
def get_point(r):
    p = 0
    dup_point = 0
    # x좌표로 생각 0부터 r-1까지의 x 좌표에 대응하는 y 좌표 확인
    for i in range(r):
        # 원의 방정식을 y에 대해 정리한 식을 표현
        p += int((r**2 - i**2)**(1/2))
        # 원 테두리 위에 존재하는 점의 개수 확인
        if ((r**2 - i**2)**(1/2))%1 == 0:
            dup_point +=1
    # 1개의 사분면에 존재하는 점의 개수를 4배를 해줌
    dup_point *= 4
    p *=4
    # (0, 0) 좌표를 더해줌
    p += 1
    return p, dup_point

# print(solution(10, 50))

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    # numbers의 요소의 형을 모두 str 형으로 변환 후 리스트로 저장
    numbers = list(map(str, numbers))
    # 요소의 *3 (str형태이니 곱하면 3번 이어붙임)를 기준으로 정렬
    numbers.sort(reverse=True, key=lambda x : x*3)
    # [0,0,0] 이 입력받으면 000이라는 문자열을 0으로 바꾸기 위한 작업 
    answer = int(''.join(numbers))
    # 다시 문자열로 바꾸어 return
    return str(answer)

numbers = [8, 30, 17, 2, 23]
print(solution(numbers))