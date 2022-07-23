import time

test_list = [x for x in range(0, 1000001)]

test_set = set([x for x in range(0, 1000001)])

t_0 = time.time()
print(1000000 in test_list)
t_1 = time.time()

print("list : {}".format(t_1 - t_0))

t_0 = time.time()
print(1000000 in test_set)
t_1 = time.time()

print("set : {}".format(t_1 - t_0))
