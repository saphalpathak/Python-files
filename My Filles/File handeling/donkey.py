with open("gada.txt","r") as f:
    a = f.read()

with open("gada.txt","w") as f:
    f.write(a.replace("donkey","#######"))
        
