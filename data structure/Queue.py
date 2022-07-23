# deque 는 파이썬 collections 모듈에서 가지고 온다
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")
queue.append("E")

print(queue)

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐 맨 앞 데이터 삭제, 리턴
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)
