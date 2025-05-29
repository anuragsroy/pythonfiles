class employee(object ):
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary

    def add_salary(self,increament):
        self.emp_salary= self.emp_salary+increament
        return self.emp_salary

emp=employee(2011,"Anurag",9000)
increament=int(input("Enter the salary increament:"))

print("The new salary is:", emp.add_salary(increament))