class Mentor:                                                       # Родительский класс (задание 1)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Leсturer (Mentor):                                            # Дочерний класс Лекторы (задание 1)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):                                             # Метод str (задание 3.1)
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.leсturer_average_grade()}'
        return result

    def leсturer_average_grade(self):                              # Средняя оценка Лектора
        grades_list = sum(self.grades.values(), start = [])
        return round(sum(grades_list) / len(grades_list), 1)

    def __lt__(self, other):                                       # Сравнение лекторов по средней оценке (задание 3.2)
        if not isinstance(other, Leсturer):
            print('Ошибка')
            return
        return self.leсturer_average_grade() < other.leсturer_average_grade()


class Reviewer (Mentor):                                             # дочерний класс Проверяющие (задание 1)
    def rate_hw(self, student, course, grade): 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]                   # Проверяющие выставляют оценки студентам (задание 2)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):                                              # Метод str (задание 3.1)
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_leсturer(self, leсturer, course, grade):                    # Студенты выставляют оценки лекторам (задание 2)
        if isinstance(leсturer, Leсturer) and course in self.courses_in_progress and course in leсturer.courses_attached:     
            if course in leсturer.grades:    
                leсturer.grades[course] += [grade]
            else:
                leсturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__ (self):                                                # Метод str (задание 3.1)
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.student_average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def student_average_grade(self):                                   # Средняя оценка студента
        grades_list = sum(self.grades.values(), start = [])
        return round(sum(grades_list) / len(grades_list), 1)

    def __lt__(self, other):                                           # Сравнение студентов по средней оценке (задание 3.2)
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.student_average_grade() < other.student_average_grade()
        

def av_grade_all_students(student_list, course):                       # Средний балл всех студентов курса (задание 4.1)
    grades = []
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                grades.extend(value)
    if len(grades) == 0:
        return f'Оценок ещё нет'
    else:           
        return sum(grades) / len(grades)            
    

def av_grade_all_lecturers(lecturers_list, course):                    # Средний балл всех лекторов курса (задание 4.2)
    grades = []
    for lecturer in lecturers_list:
        for key, value in lecturer.grades.items():
            if key == course:
                grades.extend(value)
    if len(grades) == 0:
        return f'Оценок ещё нет'
    else:           
        return sum(grades) / len(grades)


lecturer_1 = Leсturer('Евгений', 'Лосев')            # Экземпляры Лекторы 
lecturer_1.courses_attached = ['Git', 'SQl']
lecturer_2 = Leсturer('Георгий', 'Чивчян')
lecturer_2.courses_attached = ['Python']
lecturers_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Аркадий', 'Цареградцев')      # Экземпляры Проверяющие
reviewer_1.courses_attached = ['Python', 'Git', 'SQl']
reviewer_2 = Reviewer('Роман', 'Тиводар')
reviewer_2.courses_attached = ['Python', 'Git']
   
student_1 = Student('Антон', 'Козлов', 'муж')        # Экземпляры Студенты
student_1.finished_courses = ['SQl']
student_1.courses_in_progress = ['Git', 'Python']
student_2 = Student('Дамир', 'Идиятуллин', 'муж')
student_2.finished_courses = ['Git']
student_2.courses_in_progress = ['Python', 'SQl']
student_list = [student_1, student_2] 


reviewer_1.rate_hw(student_1, 'Python', 10)       # Проверяющие выставляют оценки студентам (задание 4)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'SQl', 6)
reviewer_1.rate_hw(student_1, 'SQl', 7)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'SQl', 9)
reviewer_1.rate_hw(student_2, 'SQl', 10)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 10)


student_1.rate_leсturer(lecturer_1, 'Git', 7)      # Студенты выставляют оценки лекторам (задание 4)
student_1.rate_leсturer(lecturer_1, 'Git', 10)        
student_1.rate_leсturer(lecturer_1, 'SQl', 8)
student_1.rate_leсturer(lecturer_2, 'Python', 8)
student_1.rate_leсturer(lecturer_2, 'Python', 9)
student_2.rate_leсturer(lecturer_1, 'Git', 8)
student_2.rate_leсturer(lecturer_1, 'SQl', 10)
student_2.rate_leсturer(lecturer_1, 'SQl', 8)
student_2.rate_leсturer(lecturer_2, 'Python', 9)
student_2.rate_leсturer(lecturer_2, 'Python', 10)

print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1)
print(student_2)

print(f'{reviewer_1.name} {reviewer_1.surname} ведёт курсы: {", ".join(reviewer_1.courses_attached)}')

for k, v in lecturer_1.grades.items():
    print(f'{lecturer_1.name} {lecturer_1.surname} за лекции по {k} получил оценки:', *v)

print(f'Средний балл студентов по курсу "Python": {av_grade_all_students(student_list, "Python")}')
print(f'Средний балл лекторов по курсу "Git": {av_grade_all_lecturers(lecturers_list, "Git")}')

print(f'{student_2.name} {student_2.surname} имеет средний балл: {student_2.student_average_grade()}')
print(f'{student_1.name} {student_1.surname} имеет средний балл: {student_1.student_average_grade()}')

if student_1 > student_2:
    print(f'{student_1.name} {student_1.surname} круче, чем {student_2.name} {student_2.surname}')
else:
    print(f'{student_2.name} {student_2.surname} круче, чем {student_1.name} {student_1.surname}')

print(f'{lecturer_1.name} {lecturer_1.surname} имеет средний балл за лекции: {lecturer_1.leсturer_average_grade()}')
print(f'{lecturer_2.name} {lecturer_2.surname} имеет средний балл за лекции: {lecturer_2.leсturer_average_grade()}')

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} {lecturer_1.surname} имеет более высокий средний балл за лекции, чем {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'{lecturer_2.name} {lecturer_2.surname} имеет более высокий средний балл за лекции, чем {lecturer_1.name} {lecturer_1.surname}')
