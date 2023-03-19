import random

class Student:
    def __init__(self, name):
        self.name = name
        self.rest = 50
        self.eat = 0
        self.alive = True


    def to_study(self):
        print("Cat life")
        self.eat += 0.12
        self.rest -= 5


    def to_sleep(self):
        print("Cat will sleep")
        self.rest += 3


    def to_chill(self):
        print("Rest time")
        self.rest += 5
        self.eat -= 0.1


    def is_alive(self):
        if self.eat < -0.5:
            print("Bad mood")
            self.alive = False
        elif self.rest <= 0:
            print("No interest")
            self.alive = False
        elif self.eat > 5:
            print("Good life")
            self.alive = False


    def end_of_day(self):
        print(f"Rest = {self.rest}")
        print(f"Eat = {round(self.eat, 2)}")


    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Cat")

for day in range(365):
    if nick.alive:
        nick.live(day)