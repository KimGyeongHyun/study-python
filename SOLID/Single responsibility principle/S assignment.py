class Student:
    def __init__(self, name, id, major):
        self.profile = Profile(name, id, major)
        self.grade = Grade()
        self.calc_grade = CalculateGrade(self.grade)
        self.show = Show(self.profile, self.calc_grade)


class Profile:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major


class Grade:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")


class CalculateGrade:
    def __init__(self, grade):
        self.grades = grade.grades

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)


class Show:
    def __init__(self, profile, calc_grade):
        self.profile = profile
        self.calc_grade = calc_grade

        """
        self.id = profile.id ... 이처럼 하면
        처음 초기화된 값만 들어감
        (id 가 20130024 대신 이전 것의 20120034 로 출력 됨)
        객체 자체를 받아야 서로 소통이 되는 듯함
        """


    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.profile.name, self.profile.id, self.profile.major, self.calc_grade.get_average_gpa()))


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

# 학생 성적표
younghoon.show.print_report_card()
