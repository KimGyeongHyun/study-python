class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits
        self.adjacent_stations = []     # 인접한 역 저장, 가중치는 튜플로 저장


# 지하철 역 노드 인스턴스 생성
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가역", 16)
station_3 = StationNode("서울역", 16)

# 1) 노드들을 파이썬 리스트에 저장
# 그래프는 트리와 링크드 리스트와 다르게 특정 고유값으로 효율적 접근 가능
stations = [station_0, station_1, station_2, station_3]

# 2) 지하철 역 노드들을 파이썬 딕셔너리에 저장한다
# 특정 고유값으로 효율적 접근 가능
# 키는 겹치면 안 된다는 조건 있음, 다른 데이터 써야 함
stations = {
    "교대역": station_0,
    "사당역": station_1,
    "종로3가역": station_2,
    "서울역": station_3
}