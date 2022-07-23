finished_classes = set()

# 데이터 저장
finished_classes.add("A")
finished_classes.add("B")
finished_classes.add("C")
finished_classes.add("D")
finished_classes.add("E")

print(finished_classes)

# 중복 데이터 저장 시도
finished_classes.add("A")
finished_classes.add("E")

print(finished_classes)

# 데이터 탐색
print("A" in finished_classes)
print("e" in finished_classes)

# 데이터 삭제
finished_classes.remove("B")
finished_classes.remove("D")

print(finished_classes)
