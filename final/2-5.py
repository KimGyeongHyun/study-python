# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):

    staircase_dic = {
        0: 1
    }

    for i in range(1, stairs+1):    # dic 에 추가할 index
        staircase_dic[i] = staircase_dic[i - possible_steps[0]]         # default 변수 적용
        for j in range(1, len(possible_steps)):                         # possible_steps 만큼 반복
            if i >= possible_steps[j]:                                  # index 크기가 possible_steps 이상일 경우
                staircase_dic[i] += staircase_dic[i-possible_steps[j]]  # possible_steps case 추가

    # for i in range(1, stairs+1):
    #     staircase_dic[i] = staircase_dic[i-possible_steps[0]]
    #     if i >= possible_steps[1]:
    #         staircase_dic[i] += staircase_dic[i-possible_steps[1]]
    #     if i >= possible_steps[2]:
    #         staircase_dic[i] += staircase_dic[i-possible_steps[2]]

    # for i in range(1, stairs+1):
    #     if i < possible_steps[1]:
    #         staircase_dic[i] = staircase_dic[i-possible_steps[0]]
    #     elif i < possible_steps[2]:
    #         staircase_dic[i] = staircase_dic[i-possible_steps[0]] + staircase_dic[i-possible_steps[1]]
    #     else:
    #         staircase_dic[i] = staircase_dic[i-possible_steps[0]] + staircase_dic[i-possible_steps[1]] + staircase_dic[i-possible_steps[2]]

    # print(staircase_dic)

    return staircase_dic[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))