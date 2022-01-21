with open("log.txt") as f:
    content1 = f.read()
with open("copy.txt") as f:
    content2 = f.read()
if content1 == content2:
    print("Both files are same. ")
else:
    print("These files are different.")