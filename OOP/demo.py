class Dog:
    name = "x"

    def walk(self):
        print(type(self), self)
        print("walking!")
        # return True

dog1 = Dog()
# dog1.name = "Pinky"

dog2 = Dog()
# dog2.name = "Rexy"

print(dog1.walk())
print(dog1)
# print(dog2.name)