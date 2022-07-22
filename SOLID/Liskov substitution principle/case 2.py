class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    """정사각형 클래스"""

    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    # 의도와 다르게 오버라이딩
    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    # 의도와 다르게 오버라이딩
    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1


# 리스코프 치완원칙 적용할 시 (오버라이딩이 의도와 같게 하면) 정사각형의 규칙이 깨지는 현상 발생

# 정사각형은 직사각형의 행동규약을 지키기 어려움
# 즉 상속하면 안 됨
# 상속 전에 행동규약까지 확인해야 함

rectangle_1 = Rectangle(4, 6)
rectangle_2 = Square(2)

rectangle_1.width = 3
rectangle_1.height = 7

print(rectangle_1.area())

rectangle_2.width = 3
rectangle_2.height = 7

print(rectangle_2.area())
