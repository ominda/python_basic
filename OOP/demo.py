class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self, color):
        self.color = color
        msg = f"I'm {self.name}, Woof Woof!!. I have beautiful {self.color}"
        return msg
    
    def run(self):
        msg = f"I'm {self.name}. I'm {self.age} old and I can run fast"
        return msg

dog1 = Dog("Browney", 4)
print(dog1.bark("Black"))

dog2 = Dog("Pinkey", 5)
print(dog2.run())

#####

# class Dog:
#     def __init__(self) -> None:
#         print("Hello")


# dog1 = Dog()
# dog2 = Dog()

#####

# class MyClass:
#     pass