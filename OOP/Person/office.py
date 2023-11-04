from employee import Employee

class Office(Employee):
    def __init__(self, name: str, nid: str, age: int, employee_id: int, designation: str, seat_no: int, department: str) -> None:
        """
        This is the construction function of the Office class
        """
        super().__init__(name, nid, age, employee_id, designation)
        self.seat_no = seat_no
        self.department = department


    def development(self) -> str:
        """
        This function returns a string message
        """
        msg = f"Hi, I'm {self.name}, I am a Developer sit at {self.seat_no}"
        return msg
    

    def qa(self) -> str:
        """
        This function returns a string message
        """
        msg = f"I'm QA engineer work on {self.department} department. My employee ID is {self.employee_id}"
        return msg
    

if __name__ == "__main__":
    employee1 = Office("Kevin", "943884539V", 28, 112233, "SQE", 201, "Infastructure Operations")
    print(employee1.qa())