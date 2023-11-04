class Dog():
    def __init__(self, name:str, age:int, color:str) -> None:
        """
            This is the constructor method of the Dog class
        """
        self.name = name
        self.age = age
        self.color = color


    def bark(self) -> str:
        """
            This is how dog speak!
        """
        msg = f"Hi, I'm {self.name}, I say Woof! Woof!"
        return msg


    def run(self) -> str:
        """
            This is how dogs run around!
        """
        msg = f"I'm {self.name} and {self.age} years old. I can run fast!"
        return msg
    

    def eat(self) -> str:
        """
            This is how dogs eats!
        """
        msg = f"I'm {self.name}, I like to eat meat. I'm {self.age} old and I have beautiful {self.color} colour on me!"
        return msg
    

dog1 = Dog("Browney", 5, "Brown")
dog2 = Dog("Whita", 3, "White")
dog3 = Dog("Pinkey", 7, "Black & White")

print(dog1.bark())
print(dog2.run())
print(dog3.eat())