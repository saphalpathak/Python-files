list1 = ["donkey","monkey","cat"]
with open("gada.txt","r") as f:
    a = f.read()
for name in list1:
    a = a.replace(name,"###")
    with open("gada.txt","w") as f:
        f.write(a)