a = int(input("Enter a marks in 1st subject: "))
b = int(input("Enter a marks in 2nd subject: "))
c = int(input("Enter a marks in 3rd subject: "))
per = (a+b+c)/3
if(per>=90):
    print("Your grade is Ex")
elif(per>=80):
    print("Your grade is A")
elif(per>=70):
    print("Your grade is B")
elif(per>=60):
    print("Your grade is C")
elif(per>=50):
    print("Your grade is D")
elif(per<=50):
    print("Your grade is F")