class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def speak(self):
        x = "I am {0} {1}. \nI'am {2} years old.".format(self.firstname, self.lastname, self.age)
        return x

    def talk(self):
        y = "Welcome"
        return y


class Student(Person):
    def __init__(self, firstname, lastname, age, gender):
        super().__init__(firstname, lastname, age)
        self.gender = gender

    def talk(self):
        y = "Hello"
        return y


obj1 = Person("Karen", "Karapetyan", 20)
obj2 = Student("Karen", "Karapetyan", 20, "Male")


# print(obj1.speak())
# print(obj2.speak())
# print(obj1.talk()) # Welcome
# print(obj2.talk()) # Hello


class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        z = "Beep~beep"
        return z


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        z = "Honk~honk"
        return z
