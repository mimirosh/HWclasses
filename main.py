class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached
        ):
            if 0 <= grade <= 10:
                lecturer.grades.setdefault(course, []).append(grade)
            else:
                print('Ошибка: оценка должна быть от 0 до 10')
        else:
            print('Ошибка: невозможно поставить оценку')

    def average_grade(self):
        total_grades = sum(map(sum, self.grades.values()))
        count_grades = sum(map(len, self.grades.values()))
        return round(total_grades / count_grades, 2) if count_grades else 0

    def average_grade_for_course(self, course):
        total = 0
        count = 0
        for student in Student.all_students:
            grades = student.grades.get(course, [])
            total += sum(grades)
            count += len(grades)
        return round(total / count, 2) if count else 0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress) or 'Нет'
        finished_courses = ', '.join(self.finished_courses) or 'Нет'
        avg_grade = self.average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнение невозможно, объект не является студентом.")
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print("Сравнение невозможно, объект не является студентом.")
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Сравнение невозможно, объект не является студентом.")
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.all_lecturers.append(self)

    def average_grade(self):
        total_grades = sum(map(sum, self.grades.values()))
        count_grades = sum(map(len, self.grades.values()))
        return round(total_grades / count_grades, 2) if count_grades else 0

    def average_grade_for_course(self, course):
        total = 0
        count = 0
        for lecturer in Lecturer.all_lecturers:
            grades = lecturer.grades.get(course, [])
            total += sum(grades)
            count += len(grades)
        return round(total / count, 2) if count else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg_grade}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнение невозможно, объект не является лектором.")
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнение невозможно, объект не является лектором.")
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнение невозможно, объект не является лектором.")
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress
        ):
            if 0 <= grade <= 10:
                student.grades.setdefault(course, []).append(grade)
            else:
                print('Ошибка: оценка должна быть от 0 до 10')
        else:
            print('Ошибка: невозможно поставить оценку')

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )

# Создаем по 2 экземпляра каждого класса

# Студенты
student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Мария', 'Петрова', 'женский')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Английский для программистов']

# Лекторы
lecturer1 = Lecturer('Сергей', 'Сергеев')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Алексей', 'Алексеев')
lecturer2.courses_attached += ['Git']

# Проверяющие
reviewer1 = Reviewer('Анна', 'Антонова')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Елена', 'Еленова')
reviewer2.courses_attached += ['Git']

# Вызов методов

# Проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student1, 'Git', 10)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)

student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 7)

student1.rate_lecturer(lecturer2, 'Git', 9)
student1.rate_lecturer(lecturer2, 'Git', 10)

# Вывод информации о студентах
print(student1)
print()
print(student2)
print()

# Вывод информации о лекторах
print(lecturer1)
print()
print(lecturer2)
print()

# Вывод информации о проверяющих
print(reviewer1)
print()
print(reviewer2)
print()

# Сравнение студентов
print("Сравнение студентов по средней оценке:")
if student1 > student2:
    print(f"{student1.name} {student1.surname} имеет более высокую среднюю оценку, чем {student2.name} {student2.surname}")
elif student1 < student2:
    print(f"{student2.name} {student2.surname} имеет более высокую среднюю оценку, чем {student1.name} {student1.surname}")
else:
    print(f"{student1.name} {student1.surname} и {student2.name} {student2.surname} имеют одинаковую среднюю оценку")
print()


# Сравнение лекторов
print("Сравнение лекторов по средней оценке:")
if lecturer1 > lecturer2:
    print(f"{lecturer1.name} {lecturer1.surname} имеет более высокую среднюю оценку, чем {lecturer2.name} {lecturer2.surname}")
elif lecturer1 < lecturer2:
    print(f"{lecturer2.name} {lecturer2.surname} имеет более высокую среднюю оценку, чем {lecturer1.name} {lecturer1.surname}")
else:
    print(f"{lecturer1.name} {lecturer1.surname} и {lecturer2.name} {lecturer2.surname} имеют одинаковую среднюю оценку")
print()

# Подсчет средней оценки за домашние задания по курсу 'Python'
avg_student_grade_python = student1.average_grade_for_course('Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {avg_student_grade_python}")

# Подсчет средней оценки за лекции по курсу 'Python'
avg_lecturer_grade_python = lecturer1.average_grade_for_course('Python')
print(f"Средняя оценка за лекции по курсу 'Python': {avg_lecturer_grade_python}")
