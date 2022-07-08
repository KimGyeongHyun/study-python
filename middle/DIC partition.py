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


# 퀵 정렬
def quicksort(my_list, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(my_list) - 1
    if end - start >= 1:
        pivot = partition(my_list, start, end)
        # print(my_list)
        # print(pivot)

        quicksort(my_list, start, pivot-1)
        quicksort(my_list, pivot+1, end)

# 코드를 작성하세요.


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)