class Dog():
    def __init__(self, name, age, title="hello"):
        self.name = name
        self.age = age

    def sit(self):
        print("name = " + self.name + " , sit")


mydog = Dog("anqi", 18)
mydog.sit()
