def take_input(name):
    name = []
    no_n = int(input(f"How many number you want to enter in first martix:"))
    for number in range(no_n):
        data = int(input("Enter a number: "))
        name.append(data)
    return name
def addition():
    
first = input("Enter a name of first matrix: ")
second = input("Entera name of second matrix: ")
first =take_input(first)
second = take_input(second)

