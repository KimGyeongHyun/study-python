def course_selection(course_list):

    # 코드를 작성하세요.
    final_course = []   # 최종 수업
    first_time = 0      # 이전 수업이 끝나는 시간
    temp_course = [0]   # 탐욕적 선택 코스 임시 저장

    # Greedy Algorithm
    # 앞에서부터 먼저 끝나는 수업을 선택함

    while len(temp_course) != 0:     # 조건에 맞는 코스가 없을 때까지 반복
        second_time = 24    # 탐색 중 현재 수업의 제일 일찍 끝나는 시간
        temp_course = []  # Greedy select 코스 임시 저장

        for course in course_list:  # 수업 스캔
            # 앞 수업 끝나는 시간과 중복 없고, 이전에 봤던 코스 보다 더 일찍 끝나는 경우
            if first_time <= course[0] and course[1] <= second_time:
                temp_course = course             # 코스 채택
                second_time = temp_course[1]     # 일찍 끝나는 시간 갱신

        if len(temp_course) != 0:                # 조건에 맞는 코스가 있다면
            final_course.append(temp_course)     # 해당 코스를 최종 수업에 추가
            first_time = temp_course[1]          # 다음 코스 기준 이전 코스 끝나는 시간 저장

    return final_course


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
