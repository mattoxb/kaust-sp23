#!/usr/bin/env python3


class Animal:
    def __init__(self):
        self.data = self.data + ["animal"]
        self.kind = "unknown"
        self.call = "what"
        self.legs = 0
    def speak(self):
       print("The " + self.kind + " says " + self.call)

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4
        self.kind = "cat"
        self.call = "meow"

class Dog(Animal):
    def __init__(self):
        self.data = ["dog"]
        super().__init__()
        self.legs = 4
        self.kind = "dog"
        self.call = "woff"

class Fox(Animal):
    def __init__(self):
        self.data = ["fox"]
 #      super().__init__()
        self.legs = 4
        self.kind = "fox"

# Write a Bird class that is a subclass of Animal.
# Birds should be able to fly or something.
# Make two subclasses of birds: canary, bluejay
#
