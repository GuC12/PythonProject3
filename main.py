class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50
        self.energy = 50
        self.mood = 50
    def status(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Голод: {self.hunger}")
        print(f"Энергия: {self.energy}")
        print(f"Настроение: {self.mood}")

    def sound(self):
        print("meow")
    def eat(sellf):
        print(sellf.name, "is eating")

    def walking(self):
        print(self.name, "is walking")

    def sleep(self):
        print(self.name, "is sleeping")

if __name__ == "__main__":
    cat = Cat("Мурзик", 3)
    cat.status()
print(cat.sound())
print(cat.eat())
print(cat.walking())
print(cat.sleep())
