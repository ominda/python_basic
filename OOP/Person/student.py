from person import Person

class Student(Person):
    def __init__(self, name: str, nid: str, age: int, student_id: int, stream: str) -> None:
        """
        This is the constructor method of the student class
        """
        super().__init__(name, nid, age)
        self.student_id = student_id
        self.stream = stream

    
    def learn(self):
        """
        This method just return a message!
        """
        msg = f"I'm {self.name}. I studying in {self.stream}!"
        return msg
    

    def do_exams(self):
        """
        This fuction just return a string message
        """
        msg = f"I'm {self.name}. My student ID is {self.student_id}. I do a lot of exams!"
        return msg
    

if __name__ == "__main__":
    ominda = Student("Ominda", "850591059v", 38, 10447, "Computer Science")
    print(ominda.learn())
    print(ominda.do_exams())
