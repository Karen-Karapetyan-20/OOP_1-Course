import math


class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        '''barks n time'''
        for i in range(n):
            print("Bark !")


class Math:
    @staticmethod
    def add(x1, x2):
        return x1 + x2


# tim = Dog("Tim")
# print(Dog.num_dogs())

Dog.bark(5)
