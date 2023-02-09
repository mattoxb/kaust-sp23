#!/usr/bin/env python3


class Animal:
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['animal']
        else:
            self.data = ["animal"]
        self.kind = "unknown"
        self.call = "what"
        self.legs = 0
    def speak(self):
       print("The " + self.kind + " says " + self.call)

class Cat(Animal):
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['cat']
        else:
            self.data = ["cat"]
        super().__init__()
        self.legs = 4
        self.kind = "cat"
        self.call = "meow"

class Dog(Animal):
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['dog']
        else:
            self.data = ["dog"]
        super().__init__()
        self.legs = 4
        self.kind = "dog"
        self.call = "woff"

class Fox(Animal):
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['fox']
        else:
            self.data = ["fox"]
 #      super().__init__()
        self.legs = 4
        self.kind = "fox"

# Write a Bird class that is a subclass of Animal.
# Birds should be able to fly or something.
# Make two subclasses of birds: canary, bluejay
#
class Bird(Animal):
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['bird']
        else:
            self.data = ["bird"]
        super().__init__()
        self.kind = "bird"
        self.legs = 2

    def fly(self):
        print("The " + self.kind + " is flying!")


class Chicken(Bird):
    def __init__(self):
        if 'data' in self.__dir__():
            self.data = self.data + ['chicken']
        else:
            self.data = ["chicken"]

        super().__init__()

        self.kind = "chicken"
        self.call = "brock brock brock"
