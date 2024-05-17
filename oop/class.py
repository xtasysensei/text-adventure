class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


ozzy = Dog("Ozzy", 2)

print(ozzy.name + " is " + str(ozzy.age) + " year(s) old.")
