class Point:

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# object is an instance of class
# class is a blueprint. defines new class

point1 = Point(10, 20)
point1.draw()
point1.move()

print(point1.x)
print(point1.y)

# setting variables dynamically
point1.x = 20
point1.y = 30

print(point1.x)
print(point1.y)


# inheritance
class Mammal:
    def walk(self):
        print("Is walking")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


dog = Dog()
dog.bark()