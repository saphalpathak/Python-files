import  os as o
old_name = "a.txt"
new_name = "renamed_by_python.txt"
with open(old_name) as f:
    content = f.read()
with open(new_name,"w") as f:
    content = f.write(content)
o.remove(old_name)
