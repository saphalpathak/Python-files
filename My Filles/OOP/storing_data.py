class Programmer:
    employee = "Microsoft"

    def __init__(self, name, address, salary):
        self.nam = name
        self.address = address
        self.salary = salary
    def getInfo(self):
        print(f"The name of the employee is {self.nam}, address is {self.address} and the salary is{self.salary}")


hari = Programmer("saphal","palpa","1000")
# hari.data("saphal","palpa","1000")
hari.getInfo()
