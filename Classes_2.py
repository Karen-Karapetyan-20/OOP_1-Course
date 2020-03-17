class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def speak(self):
        x = "I am {0} {1}. \nI'am {2} years old.".format(self.firstname, self.lastname, self.age)
        return x

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight
        weight = 70


obj = Person("Karen", "Karapetyan", 20)
obj.change_age(21)
print(obj.speak())
