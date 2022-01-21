with open("log.txt") as f:
    a = f.read()
if "terminated" in a:
    print("Yes, There is terminated.")
else:
    print("No, There is not terminated.")