# list 내에 두 요소의 합이 sum 이 되는지 확인 / bool return

def sum_in_list(search_sum, sorted_list):

    for number in sorted_list:
        if search_sum-number in sorted_list:
            return True

    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
