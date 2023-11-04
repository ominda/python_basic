from student import Student

class School(Student):
    

    def __init__(self, name: str, nid: str, age: int, student_id: int, stream: str, grade: str) -> None:
        """
        This is the constructor method of the School class
        """
        super().__init__(name, nid, age, student_id, stream)
        self.grade = grade


    def walk(self) -> str:
        """
        This fuction returns a string message
        """
        msg = f"This function overload the parant 'walk' function. Name is {self.name} and the age is {self.age}!"
        return msg
    

    def run(self) -> str:
        """
        This function returns a string message
        """
        msg = f"I'm {self.name}, studing at grade {self.grade}. I can run fast!!"
        return msg
    

if __name__ == "__main__":
    student1 = School("Sanda", "199023430V", 15, 1000, "Science", "Grade 10")
    print(student1.run())

    