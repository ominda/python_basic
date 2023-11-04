from employee import Employee

class Labor(Employee):
    def __init__(self, name: str, nid: str, age: int, employee_id: int, designation: str, task_id: int) -> None:
        super().__init__(name, nid, age, employee_id, designation)
        self.task_id = task_id


    def maintainance(self):
        """
        This function returns a string message
        """
        msg = f"I'm {self.name}. My employee ID is {self.employee_id}. My designation is {self.designation}"
        return msg
    

    def cleaning(self):
        """
        This function returns a string message
        """
        msg = f"I'm a {self.designation}, my task id is {self.task_id}"
        return msg
    

if __name__ == "__main__":
    employee1 = Labor("Supun", "788712342V", 48, 10, "Supervisor", 20)
    print(employee1.maintainance())