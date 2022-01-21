for mul in range(2,21):
    for num in range(1,11):
        with open(F"Table{mul}","a") as f:
            f.write(f"{mul} x {num} = {mul*num}\n")