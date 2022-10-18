class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i am {self.name}")


p = Person("Zainul Abdeen")
p.talk()