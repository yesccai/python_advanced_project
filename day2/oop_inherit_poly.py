class Animal:
    def speak(self):
        raise NotImplementedError("Sunclasses must implement this methed.")

class Dog(Animal):
    def speak(self):
        return  "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Robot(Animal):
    def speak(self):
        return "Beep boop"