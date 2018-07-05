class car:

    slogan = None
    population=0

    def __init__(self, name="Default"):
        self.name = name
        car.population+=1

    def start(self,sound):
        print(sound)

    def set_slogan(self, data):
        car.slogan= data
        print(car.slogan)

mycar = car("HELLO")
print(mycar.name)
mycar.start("BLOB BLOLB")
mycar.slogan
bhs=car("\n")
print(bhs.name)

mycar.set_slogan("DSADAAS")
car.slogan="dafds"
print(car.slogan)
print(car.population)
