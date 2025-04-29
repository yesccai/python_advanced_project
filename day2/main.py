from oop_inherit_poly import Dog, Cat, Robot

def make_it_speak(obj):
        print(obj.speak)

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    robot = Robot()

    make_it_speak(dog)
    make_it_speak(cat)
    make_it_speak(robot)
