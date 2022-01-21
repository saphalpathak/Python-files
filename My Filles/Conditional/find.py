name = ["Hari","Shyam","Geeta","sita"]
test_name = input("Enter name you want to find: ")
test_name = test_name.capitalize()
if (test_name in name):
    print("Your name is in list")
else:
    print("Your name is not in list")