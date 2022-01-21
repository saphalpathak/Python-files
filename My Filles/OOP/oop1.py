class Employee:
    company = "Google"
    def getSalary(self,signature):
        salary = self.salary
        print(salary)
        print(signature)
    def __init__(self,address,surname,salary):
        print("Hello everybody!")
        self.address = address
        self.surname = surname
        self.salary = salary
    @staticmethod
    def greet():
        print("Good Morning, Sir")
    @staticmethod
    def ram():
        print("Good Morning, Madam")
        

saphal = Employee("palpa","pathak",1000)
# krishna = Employee()
# hari = Employee()
# saphal.company = "youtube"
# saphal.salary = 700
# print(saphal.company)
# print(saphal.company)
# print(Employee.company)
# Employee.company = "Microsoft"
# print(Employee.company)
# saphal.salary = 700
# print(saphal.salary)
# Employee.salary = 400
# print(saphal.salary)
# print(hari.salar)
# saphal.getSalary("Thanks")
# saphal.greet()
# saphal.ram()
# __name__
