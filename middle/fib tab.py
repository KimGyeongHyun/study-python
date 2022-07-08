def fib_tab(n):
    # 코드를 작성하세요.

    fib_dic = {
        1: 1,
        2: 1
    }

    if n <= 2:
        return 1

    i = 3
    while i <= n:
        fib_dic[i] = fib_dic[i-2] + fib_dic[i-1]
        i += 1

    return fib_dic[i-1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))