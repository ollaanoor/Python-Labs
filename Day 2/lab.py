import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
    host="localhost",
    user=input("Enter username: "),
    password=getpass("Enter password: "),
    # user="root",
    # password="1234",
    database='python_lab2'
)
cur = mydb.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS employees(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name CHAR(50) NOT NULL,
                    last_name CHAR(50) NOT NULL,
                    age INT NOT NULL,
                    department CHAR(50) NOT NULL,
                    managed_department CHAR(50),
                    salary INT NOT NULL
                    );''')
mydb.commit()

class Employee:
    __employees = []  # Static list contains all employees
    
    def __init__(self,first_name,last_name,age,department,salary):
        # Assign values to the instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
    
        # Insert the created object to the list
        Employee.__employees.append(self)

        if list_init:
            # Insert new record in table employees in database
            query = """
            INSERT INTO employees(first_name, last_name, age, department, salary)
            VALUES(%s, %s, %s, %s, %s)
            """
            data = (first_name, last_name, age, department, salary)
            cur.execute(query, data)
            mydb.commit()

    @staticmethod
    def get_employees():
        return Employee.__employees
    
    def get_name(self):
        return (self.first_name + " " + self.last_name)

    def transfer(self,department):
        # Change employee department
        self.department = department

        # Update the database record with the update
        query = """
        UPDATE employees
        SET department = %s
        WHERE first_name = %s AND last_name = %s
        """
        data = (department, self.first_name, self.last_name)
        cur.execute(query, data)
        mydb.commit()
        print("Data updated successfully in DB")

    def fire(self):
        # Remove the employee from the shared list
        Employee.__employees.remove(self)

        # Delete its record from the database
        query = "DELETE FROM employees WHERE first_name = %s AND last_name = %s"
        data = (self.first_name, self.last_name)
        cur.execute(query, data)
        mydb.commit()
        print("Data deleted successfully from DB")


    def show(self):
        #  Prints all employee data
        print(f"\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nDepartment: {self.department}\nSalary: {self.salary}")
    
    @staticmethod
    def List_employees():
        # Select all employees and print their data
        query = "SELECT * FROM employees"
        cur.execute(query)
        result = cur.fetchall()
        
        for row in result:
            for i in range(len(row)):
                if (cur.description[i][0] == "salary") and (not(row[i-1] is None)):
                    print(f"{cur.description[i][0]}: Confidential")
                else:
                    print(f"{cur.description[i][0]}: {row[i]}")
            
            print("\n")


class Manager(Employee):
    
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        self.managed_department = managed_department
        super().__init__(first_name, last_name, age, department, salary)
        
        # Update the database record with the update to add managed department
        query = """
        UPDATE employees
        SET managed_department = %s
        WHERE first_name = %s AND last_name = %s
        """
        data = (managed_department, first_name, last_name)
        cur.execute(query, data)
        mydb.commit()

    # Print manager data
    def show(self):
        print(f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nDepartment: {self.department}\nManaged Department: {self.managed_department}\nSalary: Confidential")


# Main program -> 

# Sync Database with __employees list
list_init = False
query = "SELECT first_name, last_name, age, department, managed_department, salary FROM employees"
cur.execute(query)
result = cur.fetchall()
for row in result:
    first_name, last_name, age, department, managed_department, salary = row
    if managed_department is None: 
        Employee(first_name, last_name, age, department, salary)
    else:  
        Manager(first_name, last_name, age, department, salary, managed_department)

# Menu
while True:
    list_init = True
    #  Print a menu for the user with the valid operations
    operation = input("\nFor adding new employee, enter 'add'\
                    \nFor transfering an employee, enter 'transfer'\
                    \nFor firing an employee, enter 'fire'\
                    \nFor showing an employee data, enter 'show'\
                    \nFor showing all employees data, enter 'list'\
                    \nTo quit, enter 'q'\
                    \n> ").strip().lower()
    
    if operation == "add":
        type = input("\nIf manager press 'm'/ if employee press 'e': ").strip().lower()
        if not(type == 'm' or type == 'e'): 
            print("Invalid option\n")
        else:
            print("\nPlease enter employee data:")
            fname = input("First name: ")
            lname = input("Last name: ")
            age = input("Age: ")
            dep = input("Department: ")
            sal = input("Salary: ")
            
            if type == 'e':
                emp = Employee(fname,lname,age,dep,sal)
            elif type == 'm':
                managed_dep = input("Managed department: ")
                emp = Manager(fname,lname,age,dep,sal,managed_dep)
            
            print("\nRecord inserted to DB successfully.\n")

    elif operation == 'transfer':
        if len(Employee.get_employees()) == 0:
            print("No Employees in the database.\n")
        else:
            fname = input("Enter the first name of the employee: ").strip()
            lname = input("Enter the last name of the employee: ").strip()
            new_dep = input("Enter the new department: ").strip()

            # Search for the employee in the list
            found = False
            for emp in Employee.get_employees():
                if emp.get_name() == " ".join([fname,lname]):
                    emp.transfer(new_dep)
                    print(f"Employee {fname} {lname} has been transferred to {new_dep}.\n")
                    emp.show()
                    found = True
                    break
            
            if not(found):
                print("Employee not found.\n")

    elif operation == 'fire':
        if len(Employee.get_employees()) == 0:
            print("No Employees in the database.\n")
        else:
            fname = input("Enter the first name of the employee: ").strip()
            lname = input("Enter the last name of the employee: ").strip()

            found = False
            for emp in Employee.get_employees():
                if emp.get_name() == " ".join([fname,lname]):
                    emp.fire()
                    print(f"Employee {fname} {lname} has been fired.\n")
                    found = True
                    break
            
            if not(found):
                print("Employee not found.\n")

    elif operation == 'show':
        if len(Employee.get_employees()) == 0:
            print("No Employees in the database.\n")
        else:
            fname = input("Enter the first name of the employee: ").strip()
            lname = input("Enter the last name of the employee: ").strip()

            found = False
            for emp in Employee.get_employees():
                if emp.get_name() == " ".join([fname,lname]):
                    emp.show()
                    found = True
                    break
                
            if not(found):
                print("Employee not found.\n")


    elif operation == 'list':
        if len(Employee.get_employees()) == 0:
            print("No Employees in the database.\n")
        else:
            Employee.List_employees()

    elif operation == 'q':
        # Quit the program
        break

    else:
        print("Invalid option!\n")