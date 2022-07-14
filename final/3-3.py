# 담긴 빗물의 양을 리턴
# 시간 복잡도 O(n^2) 보다 적게, 상황에 따라 공간 복잡도 사용

def trapping_rain(buildings):

    peak_list = []      # 봉우리 index
    water_amount = 0    # 담긴 빗물의 양

    # 봉우리 index 구함
    for i in range(len(buildings)):

        if i == 0 and buildings[0] > buildings[1]:  # 첫번째
            peak_list.append(i)

        if i != 0 and i != len(buildings)-1:    # 가운데
            if buildings[i-1] < buildings[i] > buildings[i+1]:
                peak_list.append(i)

        if i == len(buildings)-1 and buildings[len(buildings)-2] < buildings[len(buildings)-1]:     # 마지막
            peak_list.append(i)

    peak_peak_list = []     # 봉우리의 봉우리 index

    # 봉우리의 봉우리 index 구함
    for i in range(len(peak_list)):

        if i == 0 and buildings[peak_list[i]] > buildings[peak_list[i+1]]:  # 첫번째
            peak_peak_list.append(i)

        if i != 0 and i != len(peak_list)-1:    # 가운데
            if buildings[peak_list[i-1]] < buildings[peak_list[i]] > buildings[peak_list[i+1]]:
                peak_peak_list.append(i)

        # 마지막
        if i == len(peak_list)-1 and buildings[peak_list[len(peak_list)-2]] < buildings[peak_list[len(peak_list)-1]]:
            peak_peak_list.append(i)

    # 봉우리의 봉우리 사이 봉우리 제거
    for i in range(len(peak_peak_list)-1):
        del peak_list[peak_peak_list[i]+1:peak_peak_list[i+1]]

    # 봉우리 사이 물의 양 계산
    for i in range(len(peak_list)-1):
        water_amount += min(buildings[peak_list[i]], buildings[peak_list[i + 1]]) * (peak_list[i+1] - peak_list[i] - 1)
        for j in range(peak_list[i]+1, peak_list[i+1]):
            water_amount -= buildings[j]

    return water_amount


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
