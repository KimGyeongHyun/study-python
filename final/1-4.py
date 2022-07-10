# list 안 중복 숫자 찾아 리턴
# 시간 효율 생각

def find_same_number(some_list):

    temp_list = []

    for number in some_list:
        if number in temp_list:
            return number
        temp_list.append(number)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
