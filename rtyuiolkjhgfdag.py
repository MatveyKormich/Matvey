import random


a = int(input('Какую еду дать коту: '))
b = int(input('Что даш попить коту: '))



class Dog:
    def __init__(self, name):
        self.name = name
        self.rest = 50
        self.eat = 0
        self.walk = 25
        self.alive = True

    def to_eat(self):
        print("Dog life")
        self.eat += 0.12
        self.rest -= 5

    def to_sleep(self):
        print("Dog will sleep")
        self.rest += 3

    def to_walk(self):
        print("Dog will walk")
        self.walk += 3
        self.eat -= 0.1

    def to_chill(self):
        print("Rest time")
        self.rest += 5
        self.eat -= 0.1

    def is_alive(self):
        if self.eat < -0.5:
            print("Bad mood")
            self.alive = False
        elif self.rest <= 0:
            print("tired")
        elif self.rest >= 100:
            print("full of energy")
            self.alive = False
        elif self.eat > 2:
            print("Good life")
            self.alive = False
        elif self.walk > 75:
            print("Good life")
            self.alive = False

    def end_of_day(self):
        print(f"Rest = {self.rest}")
        print(f"Eat = {round(self.eat, 2)}")
        print(f"Walk = {round(self.walk, 1)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 4)

        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_walk()

        self.end_of_day()
        self.is_alive()
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^3}")

nick = Dog(name="Dog")

for day in range(3):
    if nick.alive:
        nick.live(day)