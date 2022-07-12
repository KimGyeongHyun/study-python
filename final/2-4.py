# n개의 계단을 한 칸, 두 칸씩 올라가는 경우의 수
# 피보나치 수열과 동일

def staircase(n):

    staircase_dic = {
        0: 1,
        1: 1
    }

    for i in range(2, n+1):
        staircase_dic[i] = staircase_dic[i-1] + staircase_dic[i-2]

    return staircase_dic[n]


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
