
from collections import deque


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque()     # 사용할 스택 정의

    for number in range(len(string)):
        if string[number] == '(':
            stack.append(number)
        if string[number] == ')':
            if stack:
                stack.pop()
            else:
                print("문자열 {}번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다".format(number))

    while stack:
        print("문자열 {}번째 위치에 있는 괄호가 닫히지 않았습니다".format(stack.pop()))


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)