from collections import deque

stack = deque()
# stack = [] 로 써도 돌아감
# 자료 구조만 다를 뿐 시간복잡도와 기능은 같음

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
# Queue 와 결정적인 차이
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
