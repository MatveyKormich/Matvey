class Student:
    def __init__(self, name: str, age: int = 0, country: str = 'France') -> None:
        self.name = name
        self.age = age
        self.country = country


    def __str__(self):
        return f'Hello! My name is {self.name}. I am {self.age} years old. I am from {self.country}.'

    def print_data(self) -> None:
        print(f'Hello! My name is {self.name}. I am {self.age} years old. I am from {self.country}.')

first_student = Student(name ='Nick', age=20, country= 'USA')
second_student = Student('Kate', 19, 'Ukraine')
third_student = Student('Al', age=54)

print(first_student)
print(second_student)
print(third_student)


