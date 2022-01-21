a = True
with open("log.txt") as f:
    while a:
        a = f.readline()
        with open("copy.txt","a") as f1:
            f1.write(a)

