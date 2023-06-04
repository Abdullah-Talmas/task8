class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
# Create a Student object
john = Student("John", 20, "New York")

# Access attributes
print(john.name)  # Output: John
print(john.age)   # Output: 20
print(john.city)  # Output: New York

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        return self.marks

    def calc_average(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks)
        average = total_marks / len(self.marks)
        return average
# Create a Student object
john = Student("John", 20, "New York")

# Add marks
john.add_mark(85)
john.add_mark(90)
john.add_mark(95)

# Get all marks
all_marks = john.get_all_marks()
print(all_marks)  # Output: [85, 90, 95]

# Calculate average
average = john.calc_average()
print(average)  # Output: 90.0
