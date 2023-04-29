
def checker(function):
    def checker(*args, **kwargs): # передаём параметры
        try:
            result = function(*args, **kwargs)# пробуем получить результат от функции calculate
        except Exception as exc:# любое исключение
            print(f"No have problems {exc}")# если всё хорошо
        else:
            print(f"No problems. Result - {result}") # если что-то не так

    return checker


@checker
def calculate(expression): # функция
    return eval(expression)


calculate('2+2*4/4')
calculate('2**5-n')# n - непонятное число










