class car:
    def __init__(self, color="White", slogan= "JAI GURU DEV", doors = 4):
        self.doors = doors
        self.seats = 4
        self.color = color
        self.slogan = slogan
        self.nox=True

    def start(self):
        print("I am car , odsadsfdsfmksdfklsdf")

    def acc(self):
        print("dasdsadsfdskfdskj")

    def stop(self):
        print("I Am stoping dsf sd ")

    def __add__(self, other):
        return self.seats - other.seats

first= car()
print(first.color)

second = car("Red")
print(second.color)

third=car(slogan="HELLO")
print(third.color,third.slogan,third.doors , sep="....")

class maruti(car):

    def __init__(self,abs=True, color="White", slogan= "JAI GURU DEV"):
        super().__init__(color, slogan)
        self.seats = 5
        self.abs=abs

    def honk(self):
        print("pee pee poo poo")

    def start(self):
        super().start()
        print("I am maruti ,I run like a horse")

third.start()

fourth = maruti(True, slogan="HELLO GUYS " , color="PINK")
fourth.honk()
fourth.start()
fourth.acc()
print(fourth.color)
fourth.start()
print(fourth.doors)
print(fourth.seats)
print(fourth.abs,fourth.slogan,fourth.color)
fourth.start()



x = first + fourth
print(x)