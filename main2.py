import subject_module
subject = subject_module.Subject("Math", 90)

import student_module
student = student_module.Student("John", 20, "New York")


class Subject:
    def __init__(self, name, mark):
        self.name = name


subject1 = Subject("Math", 90)
subject2 = Subject("Science", 85)
subject3 = Subject("English", 95)
print(subject1.name)
print(subject1.mark)

print(subject2.name)
print(subject2.mark)

print(subject3.name)
print(subject3.mark)


class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


student1 = Student("John", 20, "New York")
student2 = Student("Alice", 22, "London")
student3 = Student("Michael", 19, "Paris")
print(student1.name)
print(student1.age)
print(student1.city)

print(student2.name)
print(student2.age)
print(student2.city)

print(student3.name)
print(student3.age)
print(student3.city)
