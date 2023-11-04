from student import Student

class Univercity(Student):

    def __init__(self, name: str, nid: str, age: int, student_id: int, stream: str, year: int) -> None:
        super().__init__(name, nid, age, student_id, stream)
        self.year = year

    
    def projects(self) -> str:
        """
        This function returns a string message
        """
        msg = f"I'm a Univirsity student, Student ID is {self.student_id}. I'm studing {self.stream} stream!"
        return msg
    

    def sports(self) -> str:
        """
        This function returns a string message
        """
        msg = f"In the university we can do a lot of sports. I'm in {self.year}rd year and {self.age} years Old!"
        return msg
    

if __name__ == "__main__":
    student1 = Univercity("Methu", "123456789V", 18, 12345, "Mathamatics", 3)
    print(student1.sports())