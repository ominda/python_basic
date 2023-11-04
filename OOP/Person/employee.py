from person import Person

class Employee(Person):
    def __init__(self, name: str, nid: str, age: int, employee_id: int, designation: str) -> None:
        super().__init__(name, nid, age)
        self.employee_id = employee_id
        self.designation = designation


    def work(self) -> str:
        """
        This function returns a string message!
        """
        msg = f"I'm {self.name}. I'm working as {self.designation}."
        return msg
    

    def write(self) -> str:
        """
        This function returns a string message!
        """
        msg = f"I'm {self.name} with {self.nid}. I'm working at Dialog. My Employment ID is {self.employee_id}"
        return msg
    

if __name__ == "__main__":
    rasanga = Employee("Rasanga", "826510298V", 40, 9872, "Senior Manager")
    print(rasanga.write())