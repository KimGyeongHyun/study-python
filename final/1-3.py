# capacity 만큼 최대 전진 할 수 있으며, 리스트를 건너 뛰며 최대한 멀리 감
# 들러야 하는 list 를 리턴

def select_stops(water_stops, capacity):

    term = 0            # 이전에 들른 곳을 임시로 저장
    final_list = []     # 들른 곳의 최종 리스트

    for i in range(len(water_stops)):   # water_stops 만큼 반복
        if i == len(water_stops)-1:                 # 마지막 지점일 경우
            final_list.append(water_stops[i])       # 추가
        else:                                       # 마지막 지점 아닐 경우
            if capacity < water_stops[i+1] - term:  # 이전에 들른 곳과 다음에 들를 곳의 차이가 capacity 보다 크다면
                term = water_stops[i]
                final_list.append(water_stops[i])   # 지금 있는 곳을 term, final_list 에 저장

    return final_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))