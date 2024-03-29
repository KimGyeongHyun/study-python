# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp_value = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp_value

    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    b = start
    pivot = my_list[end]
    for i in range(start, end):
        if my_list[i] < pivot:
            my_list = swap_elements(my_list, b, i)
            b += 1
        # print(i)
        # print(my_list)

    swap_elements(my_list, b, end)
    # print(my_list)
    return b

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
