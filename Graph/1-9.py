# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 코드를 쓰세요
adjacency_matrix[0][1] = 1
adjacency_matrix[0][2] = 1
adjacency_matrix[1][3] = 1
adjacency_matrix[1][5] = 1
adjacency_matrix[2][5] = 1
adjacency_matrix[3][4] = 1
adjacency_matrix[3][5] = 1
adjacency_matrix[4][5] = 1

for i in range(1, 6): # 1, 2, 3, 4, 5
    for j in range(i): # 1, 1, 2, 1, 2, 3 ...
        adjacency_matrix[i][j] = adjacency_matrix[j][i]

print(adjacency_matrix)