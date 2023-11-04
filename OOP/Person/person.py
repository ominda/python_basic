class Person:


    def __init__(self, name:str, nid:str, age:int) -> None:
        """
        Constructor method of the Person class
        """
        self.name = name
        self.nid = nid
        self.age = age


    def walk(self) -> str:
        """
        Every person can walk, we going to print some message with this function
        """
        msg = f"Hi, I'm {self.name}. I'm {self.age} old. I can walk fast"
        return msg


    def talk(self) -> str:
        """
        Every person can talk, We going to print some message with this fuction
        """
        msg = f"Hi, I'm {self.name}. my National ID number is {self.nid}. I can talk hours!"
        return msg
    

if __name__ == "__main__":
    person1 = Person("Nuwan", "859483742V", 38)
    print(person1.talk())