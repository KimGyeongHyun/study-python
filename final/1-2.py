# x^y 리턴
# O(lgy) 로 시간복잡도 줄이기

def power(x, y):

    if y == 1:
        return x

    return power(x, y//2) * power(x, y - y//2)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))