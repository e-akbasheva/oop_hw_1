class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def average_grade(self):
        grades_list = sum((list(self.grades.values())),[])
        average = 0
        for grade in grades_list:
            average += grade
        return round(average/(len(grades_list)), 1)
    
    def rate_lecture(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"
        
    def __lt__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() < student.average_grade())
        else:
            return 'Ошибка'
    
    def __le__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() <= student.average_grade())
        else:
            return 'Ошибка'
    
    def __eq__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() == student.average_grade())
        else:
            return 'Ошибка'
    
    def __ne__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() != student.average_grade())
        else:
            return 'Ошибка'
    
    def __ge__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() >= student.average_grade())
        else:
            return 'Ошибка'
    
    def __gt__(self, student):
        if isinstance(student, Student):
            return (self.average_grade() > student.average_grade())
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
          
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        grades_list = sum((list(self.grades.values())),[])
        average = 0
        for grade in grades_list:
            average += grade
        return round(average/(len(grades_list)), 1)
    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}"
    
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() < lecturer.average_grade())
        else:
            return 'Ошибка'
    
    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() <= lecturer.average_grade())
        else:
            return 'Ошибка'
    
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() == lecturer.average_grade())
        else:
            return 'Ошибка'
    
    def __ne__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() != lecturer.average_grade())
        else:
            return 'Ошибка'
    
    def __ge__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() >= lecturer.average_grade())
        else:
            return 'Ошибка'
    
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return (self.average_grade() > lecturer.average_grade())
        else:
            return 'Ошибка'
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Git']

student_2 = Student('Gou', 'Yun', 'female')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']
 
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Every', 'Buddy')
reviewer_2.courses_attached += ['Java', 'Git']

lecturer_1 = Lecturer('First', 'Speaker')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Second', 'Speaker')
lecturer_2.courses_attached += ['Java', 'Python']
 
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 10)
 
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 10)

student_1.rate_lecture(lecturer_2, 'Java', 10)
student_1.rate_lecture(lecturer_2, 'Java', 8)

student_1.rate_lecture(lecturer_2, 'Python', 6)

student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 8)

student_2.rate_lecture(lecturer_1, 'Git', 8)
student_2.rate_lecture(lecturer_1, 'Git', 6)

student_2.rate_lecture(lecturer_2, 'Python', 4)
student_2.rate_lecture(lecturer_2, 'Python', 5)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_1 < student_2)
print(student_1 <= student_2)
print(student_1 == student_2)
print(student_1 != student_2)
print(student_1 >= student_2)
print(student_1 > student_2)

print(lecturer_1 < lecturer_2)
print(lecturer_1 <= lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 > lecturer_2)

def average_hw(students: list, course: str):
    all_grades = []
    for student in students:
        all_grades += student.grades.get(course, [])
    sum = 0
    for grade in all_grades:
        sum += grade
    return f"Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {round(sum/len(all_grades), 1)}"

def average_lecture(lecturers: list, course: str):
    all_grades = []
    for lecturer in lecturers:
        all_grades += lecturer.grades.get(course, [])
    sum = 0
    for grade in all_grades:
        sum += grade
    return f"Средняя оценка за лекции всех лекторов в рамках курса {course}: {round(sum/len(all_grades), 1)}"

print(average_hw([student_1, student_2], 'Python'))
print(average_lecture([lecturer_1, lecturer_2], 'Python'))
