# 리스트 중복 수 하나만 리턴
# 공간복잡도 O(n) 이상 불가 (dic, list 활용 불가)
# some_list 변형 불가

def find_same_number(some_list, start=0, end=None):
    # divide 후 conquer
    # conquer 작업 : 중복이 있다면 int return
    # 리턴 형식이 int 라면 (중복 수가 있다면) combine 에서 해당 수를 다시 리턴

    if end is None:
        end = len(some_list)-1

    mid = start + (end - start) // 2
    # print('input <- start : {}, end : {}'.format(start, end))
    if start != mid and mid != end:
        if type(find_same_number(some_list, start, mid)) == int:
            # value = find_same_number(some_list, start, mid)
            # print('start : {}, mid : {}, return : {}'.format(start, mid, value))
            return find_same_number(some_list, start, mid)
        if type(find_same_number(some_list, mid+1, end)) == int:
            # value = find_same_number(some_list, mid+1, end)
            # print('mid : {}, end : {}, return : {}'.format(mid, end, value))
            return find_same_number(some_list, mid+1, end)

    for i in range(start, mid+1):
        for j in range(mid+1, end+1):
            if some_list[i] == some_list[j]:
                # print('start : {}, end : {}, return : {}'.format(start, end, some_list[i]))
                return some_list[i]


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
