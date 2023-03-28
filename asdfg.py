import inspect
import requests
import sys

print(sys.platform)
print(sys.argv)
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
for _ in dir(__builtins__):
    print(_)
    print(module_name, module_path)
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
def first_function():
    pass

class Human:
    pass

rq = requests
first_f = first_function
nick = Human

print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)

print(__name__)

intro_list = []
for method in dir(intro_list):
    print(method)
for method in dir():
    print(method)

data = 'string'
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

data = "string"
print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))

data = "string"
def first_function():
    pass

print(callable(data))
print(callable(first_function))

class First_class:
    pass

class Second_class(First_class):
    pass

class Second_class(First_class):
    pass

obj_from_class_2 = Second_class()

print(issubclass(obj_from_class_2, First_class))
print(issubclass(obj_from_class_2, Second_class))

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

class Human:
    def __init__(self, age, height, name = "John"):
        self.age = age
        self.name = name
        self.secondname = "Wick"
sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)

















