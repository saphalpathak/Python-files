class Calculator:
    def __init__(self,num):
        print("Welcome to simple calculator!")
        self.num = num
    def ans(self):
        square = self.num**2
        cube = self.num**3
        print(f"The square of {self.num} is {square} and the cube is {cube} ")
         


data = Calculator(4)
data.ans()