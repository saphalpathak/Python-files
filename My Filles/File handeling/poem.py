with open("poem.txt","r") as f:
    a = f.read()
if "twinkle" in a:
    print("Twinkle is in poem")
else:
    print("Twinkle is not in poem")