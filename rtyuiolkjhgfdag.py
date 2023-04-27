import random











a = int(input('Какую еду дать коту: '))
b = int(input('Что даш попить коту: '))











class Dog:
    def eat(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, eat):
                    raise ValueError('Кот останется без еды ')
            return function(*args)

        return wrapped

    @eat
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^3}")

nick = Dog(name="Dog")

for day in range(3):
    if nick.alive:
        nick.live(day)