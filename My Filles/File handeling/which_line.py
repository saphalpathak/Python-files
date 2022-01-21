a = True

with open("log.txt") as f:
    line_number = 1
    while a:
        a = f.readline()
        if "Entering" in a:
            print(f"Entering is in line {line_number}")
        line_number +=1
        