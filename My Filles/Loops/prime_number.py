num = int(input("Enter a number you want to know prime or not: "))
for i in range(2,num):
    if(num%i==0):
        print("The number is not prime number")
        break
else:
    print("The number is prime number")
    
