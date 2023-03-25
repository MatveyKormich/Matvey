class Student:
    def __init__(self, name: str, age: int = 0, country: str = 'Bulgaria',) -> None:
        self.name = name
        self.age = age
        self.country = country
        self.neme = name



    def __str__(self):
        return f'Hello {self.neme}! My name is {self.name}. I am {self.age} years old. I am from {self.country}.'

    def print_data(self) -> None:
        print(f'Hello {self.neme}! My name is {self.name}. I am {self.age} years old. I am from {self.country}.')

first_student = Student(name ='Susan', age=31, country= 'Italy')
second_student = Student('Bob', 64, 'France')
third_student = Student('Tom', age=26)

print(first_student)
print(second_student)
print(third_student)