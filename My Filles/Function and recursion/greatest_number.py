def greatest_number(num1, num2, num3):
    if(num1>num2):
        f1 = num1
    else: 
        f1 = num2
    if(f1>num3):
        f2 = f1
    else:
        f2 = num3
    print(f2)
greatest_number(9225, 8, 17)