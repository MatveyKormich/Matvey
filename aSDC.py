class Student:
    def __init__(self, name: str,name2: str, age: int = 0, country: str = 'Bulgaria') -> None:
        self.name = name
        self.age = age
        self.country = country
        self.name2 = name2



    def __str__(self):
        return f'Hello {self.name2}! My name is {self.name}. I am {self.age} years old. I am from {self.country}.'

    def print_data(self) -> None:
        print(f'Hello {self.name2}! My name is {self.name}. I am {self.age} years old. I am from {self.country}.')

first_student = Student(name ='Susan',name2 = 'Bob', age=31, country= 'Italy')
second_student = Student('Bob','Susan', 64, 'France')
third_student = Student('Tom','Bob' ,age=26)

print(first_student)
print(second_student)
print(third_student)