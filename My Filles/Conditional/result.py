math = int(input("Enter a marks of math: "))
science = int(input("Enter a marks of science: "))
social = int(input("Enter a marks of social: "))
per = (math+science+social)/3
if(math>33 and science>33 and social>33 and per>40):
    res = "Pass"
else:
    res = "Fail"
print(f"You are {res}")